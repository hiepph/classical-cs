#include <stdio.h>
#include <stdlib.h>
#include "priority_queue.h"

#define INITIAL_ARRAY_SIZE 4

#define panic(msg, ...) { \
    fprintf(stderr, "ERROR: %s", (msg), ##__VA_ARGS__); \
    exit(1); \
  }
#define check_addr(x) { if ((x) == NULL) panic("Unable to allocate memory"); }

struct node
{
  int priority;
  int value;
};

struct heap
{
  node_t **data;
  int len;
  int capacity;
};

heap_t *
heap_new()
{
  heap_t *h = calloc(1, sizeof(heap_t));

  h->capacity = INITIAL_ARRAY_SIZE;
  h->data = malloc(h->capacity * sizeof(node_t *));
  check_addr(h->data);

  return h;
}

void
heap_destroy(heap_t * h)
{
  for (int i = 0; i < h->len; i++) {
    free(h->data[i]);
  }
  free(h->data);
  free(h);
}

/*
 * Calculate the parent index given the child index
 */
int
parent_index(int idx)
{
  if (idx % 2 == 0)
    return idx / 2 - 1;
  return idx / 2;
}

/*
 * Calculate the left child index given the parent index
 */
int
left_child_index(int idx)
{
  return 2 * idx + 1;
}

/*
 * Calculate the right child index given the parent index
 */
int
right_child_index(int idx)
{
  return 2 * idx + 2;
}

void
swap_node(heap_t * h, int ia, int ib)
{
  node_t *temp = h->data[ia];

  h->data[ia] = h->data[ib];
  h->data[ib] = temp;
}

void
sift_up(heap_t * h, int idx)
{
  int parent_idx;

  while (idx > 0) {
    parent_idx = parent_index(idx);

    if (h->data[parent_idx]->priority >= h->data[idx]->priority)
      break;
    swap_node(h, idx, parent_idx);

    idx = parent_idx;
  }
}

/*
 * Resize the data storage array if needed
 */
void
heap_put(heap_t * h, int priority, int val)
{
  node_t *new_node = malloc(sizeof(new_node));
  int idx;

  check_addr(new_node);
  new_node->priority = priority;
  new_node->value = val;

  h->len++;
  if (h->len > h->capacity) {
    h->capacity = h->capacity * 2;
    h->data = realloc(h->data, h->capacity * sizeof(node_t *));
  }

  idx = h->len - 1;
  h->data[idx] = new_node;
  sift_up(h, idx);
}

void
sift_down(heap_t * h, int idx)
{
  int max_idx = idx;
  int l = left_child_index(idx);
  int r = right_child_index(idx);

  if (l < h->len && h->data[l]->priority > h->data[max_idx]->priority)
    max_idx = l;
  if (r < h->len && h->data[r]->priority > h->data[max_idx]->priority)
    max_idx = r;

  if (idx != max_idx) {
    swap_node(h, idx, max_idx);
    sift_down(h, max_idx);
  }
}

int
heap_pop(heap_t * h)
{
  int max_value = h->data[0]->value;

  h->data[0] = h->data[--h->len];

  sift_down(h, 0);

  return max_value;
}
