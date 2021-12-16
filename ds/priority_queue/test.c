#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "priority_queue.h"

void
assert_equal(int a, int b)
{
  if (a != b) {
    printf("Want: %d, Got: %d", a, b);
    exit(EXIT_FAILURE);
  }
}

int
main(void)
{
  heap_t *h = heap_new();

  /* empty */
  assert(heap_is_empty(h));

  /* put */
  heap_put(h, 1, 1);
  heap_put(h, 3, 3);
  heap_put(h, 5, 5);

  /* pop */
  assert_equal(heap_pop(h), 5);
  assert_equal(heap_pop(h), 3);

  /* resize */
  heap_put(h, 5, 5);
  heap_put(h, 3, 3);
  heap_put(h, 0, 0);
  heap_put(h, 2, 2);
  heap_put(h, 4, 4);

  heap_put(h, 6, 6);
  assert_equal(heap_pop(h), 6);

  heap_pop(h);			// 5
  heap_pop(h);			// 3
  heap_pop(h);			// 4
  heap_pop(h);			// 2
  heap_pop(h);			// 1
  heap_pop(h);			// 0
  assert(heap_is_empty(h));

  heap_destroy(h);
  return 0;
}
