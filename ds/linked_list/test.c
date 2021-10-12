#include "linkedlist.c"
#include "linkedlist.h"
#include <assert.h>

void
test_size()
{
  node_t * head = NULL;
  assert(l_size(head) == 0);

  node_t *first = malloc(sizeof(node_t));
  check_addr(first);

  first->value = 1;
  first->next = NULL;
  head = first;

  assert(l_size(head) == 1);

  l_destroy(head);
}

int
main(void)
{
  test_size();

  return 0;
}
