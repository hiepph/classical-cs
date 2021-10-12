#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define STACK_EMPTY (0)

struct list {
  struct list *next;
  int value;
};

typedef struct list *Stack;

// push value to the top of the stack
void stack_push(Stack *s, int value)
{
  // link to linked list
  // allocate memory
  // assign value
  struct list *l;

  l = malloc(sizeof(struct list));
  assert(l);

  l->value = value;
  l->next = *s;
  *s = l;
}


void stack_print(Stack *s)
{
  struct list *l;

  for (l = *s; l != 0; l=l->next) {
    printf("%d ", l->value);
  }

  putchar('\n');
}

int stack_empty(Stack *s)
{
  return *s == 0;
}

// pop the value from the top of the stack
int stack_pop(Stack *s)
{
  int v;
  struct list *l;

  assert(!stack_empty(s));

  v = (*s)->value;

  l = *s;
  *s = (*s)->next;
  free(l);

  return v;
}


int main(int argc, char** argv)
{
  int i;
  Stack s;

  s = STACK_EMPTY;

  for (i = 0; i < 5; ++i) {
    stack_push(&s, i);
    stack_print(&s);
  }

  while (!stack_empty(&s)) {
    stack_pop(&s);
    stack_print(&s);
  }

  return 0;
}
