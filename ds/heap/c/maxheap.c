#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "maxheap.h"

#define MAX_HEAP_MAXSIZE 1000
#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(EXIT_FAILURE); }

/*
 * Store the binary heap as an array.
 *
 * Keys:
 * + `size`: keep track of the current number of elements.
 * The elements belong to the heap are only inside `data[:size]`
 *
 */
struct max_heap
{
  int size;
  int data[MAX_HEAP_MAXSIZE];
  int capacity;
};

/*
 * Helper for swapping two integers
 */
void
swap(int *a, int *b)
{
  int temp = *a;

  *a = *b;
  *b = temp;
}

max_heap_t
heap_new(int capacity)
{
  max_heap_t heap;

  heap.size = 0;
  if (capacity > MAX_HEAP_MAXSIZE) {
    panic("Cannot allocate memory for a large capacity.");
  }
  heap.capacity = capacity;

  return heap;
}

/*
 * Calculate the parent index given the child index
 */
int
heap_parent_index(int idx)
{
  if (idx % 2 == 0)
    return idx / 2 - 1;
  return idx / 2;
}

/*
 * Calculate the left child index given the parent index
 */
int
heap_left_child_index(int idx)
{
  return 2 * idx + 1;
}

/*
 * Calculate the right child index given the parent index
 */
int
heap_right_child_index(int idx)
{
  return 2 * idx + 2;
}

/*
 * Sift up an element given the index
 */
void
heap_sift_up(max_heap_t * heap, int idx)
{
  int parent_idx;

  while (idx > 0) {
    parent_idx = heap_parent_index(idx);

    if (heap->data[parent_idx] >= heap->data[idx])
      break;
    swap(&heap->data[idx], &heap->data[parent_idx]);

    idx = parent_idx;
  }
}

/*
 * Sift down an element given the index
 */
void
heap_sift_down(max_heap_t * heap, int idx)
{
  int max_idx = idx;
  int l = heap_left_child_index(idx);
  int r = heap_right_child_index(idx);

  if (l < heap->size && heap->data[l] > heap->data[max_idx])
    max_idx = l;
  if (r < heap->size && heap->data[r] > heap->data[max_idx])
    max_idx = r;

  if (idx != max_idx) {
    swap(&heap->data[idx], &heap->data[max_idx]);
    heap_sift_down(heap, max_idx);
  }
}

void
heap_insert(max_heap_t * heap, int value)
{
  if (heap->size == heap->capacity) {
    panic("The heap is full.");
  }
  heap->size++;

  int idx = heap->size - 1;

  heap->data[idx] = value;
  heap_sift_up(heap, idx);
}

/*
 * Helper to print out the data of heap in array form
 */
void
heap_print(max_heap_t heap)
{
  for (int i = 0; i < heap.size; i++) {
    printf("%d ", heap.data[i]);
  }
  printf("\n");
}

int
heap_get_size(max_heap_t heap)
{
  return heap.size;
}

int
heap_get_max(max_heap_t heap)
{
  return heap.data[0];
}

/*
 * Swap max value (root) with the right-most leaf, remove the leaf
 * and sift down new root
 */
int
heap_extract_max(max_heap_t * heap)
{
  int max_value = heap->data[0];

  heap->data[0] = heap->data[heap->size - 1];
  heap->size = heap->size - 1;

  heap_sift_down(heap, 0);

  return max_value;
}

/*
 * Change the value to +inf, sift it up.
 * Extract max
 */
void
heap_remove(max_heap_t * heap, int idx)
{
  heap->data[idx] = INT_MAX;
  heap_sift_up(heap, idx);
  heap_extract_max(heap);
}
