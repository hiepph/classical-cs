#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

struct list {
  struct list *next;
  int value;
};

typedef struct queue {
  struct list *head;
  struct list *tail;
} Queue;

Queue* queue_new()
{
  Queue* q;
  q = malloc(sizeof(Queue));
  assert(q);
  q->head = q->tail = 0;
  return q;
}

void queue_enque(Queue* q, int value)
{
  struct list *l;
  l = malloc(sizeof(struct list));
  assert(l);
  l->next = 0;
  l->value = value;

  if (q->head == 0) {
    q->head = l;
  } else {
    q->tail->next = l;
  }

  q->tail = l;
}

void queue_print(Queue* q)
{
  struct list *l;
  for(l = q->head; l != 0; l=l->next) {
    printf("%d ", l->value);
  }

  putchar('\n');
}

int queue_empty(const Queue* q)
{
  return q->head == 0;
}

int queue_deque(Queue* q)
{
  struct list *l;
  int v;

  assert(!queue_empty(q));

  v = q->head->value;

  l = q->head;
  q->head = q->head->next;
  free(l);

  return v;
}

int main(int argc, char** argv)
{
  int i;
  Queue *q;

  q = queue_new();

  for (i = 0; i < 5; i++) {
    queue_enque(q, i);
    queue_print(q);
  }

  while (!queue_empty(q)) {
    queue_deque(q);
    queue_print(q);
  }

  return 0;
}
