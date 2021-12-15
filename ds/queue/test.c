#include <assert.h>
#include "queue.h"

int
main(void)
{
  queue_t *q = queue_new();
  queue_put(q, 1);
  assert(queue_peek(q) == 1);
  queue_put(q, 4);
  queue_put(q, -2);
  queue_put(q, 0);
  assert(queue_peek(q) == 1);

  assert(queue_pop(q) == 1);
  assert(queue_pop(q) == 4);
  assert(queue_pop(q) == -2);

  queue_destroy(q);
  return 0;
}
