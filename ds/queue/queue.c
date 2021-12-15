#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "queue.h"

#define panic(msg, ...) { \
    fprintf(stderr, "ERROR: %s", (msg), ##__VA_ARGS__); \
    exit(1); \
  }
#define check_addr(x) { if ((x) == NULL) panic("Unable to allocate memory"); }
#define INITIAL_ARRAY_SIZE 4

typedef struct node {
  struct node *next;
  int value;
} node_t;

/*
 * *tail is for putting new item (enqueue)
 * *head is for popping item (dequeue)
 */
struct queue
{
  node_t *head;
  node_t *tail;
};

queue_t *
queue_new()
{
  queue_t *q = malloc(sizeof(queue_t));
  check_addr(q);
  q->head = q->tail = NULL;
  return q;
}

void
queue_put(queue_t * q, int x)
{
  node_t *new_node = malloc(sizeof(node_t));

  check_addr(new_node);
  new_node->value = x;
  new_node->next = NULL;

  if (queue_is_empty(q)) {
    q->head = new_node;
  } else {
    q->tail->next = new_node;
  }

  q->tail = new_node;
}

int
queue_peek(queue_t * q)
{
  return q->head->value;
}

int
queue_pop(queue_t *q)
{
  node_t *node;
  int val;

  assert(!queue_is_empty(q));
  val = queue_peek(q);

  node = q->head;
  q->head = q->head->next;
  free(node);

  return val;
}

int
queue_is_empty(queue_t * q)
{
  return q->head == NULL;
}

void
queue_destroy(queue_t * q)
{
  while (!queue_is_empty(q)) {
    queue_pop(q);
  }
  free(q);
}
