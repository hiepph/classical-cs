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


int
parent_index(int idx)
{
  if (idx % 2 == 0)
    return idx / 2 - 1;
  return idx / 2;
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

int
heap_pop(heap_t * h)
{
  int max_value = h->data[0]->value;

  return max_value;
}
