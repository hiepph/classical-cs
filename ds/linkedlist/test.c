#include "linkedlist.c"
#include "linkedlist.h"
#include <assert.h>

void
test_size()
{
  node_t *head = NULL;

  assert(l_size(head) == 0);

  node_t *first = malloc(sizeof(node_t));

  check_addr(first);

  first->value = 1;
  first->next = NULL;
  head = first;

  assert(l_size(head) == 1);

  l_destroy(head);
}

void
test_is_empty()
{
  node_t *head = NULL;

  assert(l_is_empty(head));
  l_destroy(head);
}

void
test_push_front()
{
  node_t *head = NULL;

  head = l_push_front(head, 1);
  head = l_push_front(head, 2);

  assert(l_size(head) == 2);

  assert(head->value == 2);

  l_destroy(head);
}

void
test_value_at()
{
  node_t *head = NULL;

  head = l_push_front(head, 1);
  assert(l_value_at(head, 0) == 1);

  l_destroy(head);
}

void
test_pop_front()
{
  node_t *head = NULL;

  head = l_push_front(head, 1);
  head = l_push_front(head, 2);
  assert(l_pop_front(&head) == 2);
  assert(l_size(head) == 1);

  l_destroy(head);
}

void
test_push_back()
{
  node_t *head = NULL;

  head = l_push_back(head, 1);
  head = l_push_back(head, 2);
  assert(l_size(head) == 2);
  assert(head->value == 1);

  l_destroy(head);
}

void
test_pop_back()
{
  node_t *head = NULL;

  head = l_push_back(head, 1);
  assert(l_pop_back(&head) == 1);
  assert(l_is_empty(head));
}

void
test_insert_at()
{
  node_t *head = NULL;

  /* 2 3 1 */
  head = l_insert_at(head, 0, 1);
  head = l_insert_at(head, 0, 2);
  head = l_insert_at(head, 1, 3);
  assert(l_size(head) == 3);
  assert(l_value_at(head, 1) == 3);

  /* 2 3 4 1 */
  head = l_insert_at(head, 2, 4);
  assert(l_value_at(head, 2) == 4);

  l_destroy(head);
}

void
test_delete_at()
{
  node_t *head = NULL;

  /* 1 2 3 */
  head = l_push_back(head, 1);
  head = l_push_back(head, 2);
  head = l_push_back(head, 3);

  /* 1 3 */
  head = l_delete_at(head, 1);
  assert(l_size(head) == 2);
  assert(l_value_at(head, 1) == 3);

  l_destroy(head);
}

int
main(void)
{
  test_size();
  test_is_empty();
  test_push_front();
  test_pop_front();
  test_push_back();
  test_pop_back();
  test_insert_at();
  test_delete_at();

  return 0;
}
