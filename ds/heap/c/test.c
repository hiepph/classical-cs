#include <assert.h>
#include "maxheap.c"

int
main(void)
{
  /* new */
  max_heap_t heap = heap_new(MAX_HEAP_MAXSIZE);

  assert(heap.size == 0);
  assert(heap.capacity == MAX_HEAP_MAXSIZE);

  /* insert */
  heap_insert(&heap, 4);
  heap_insert(&heap, 14);
  heap_insert(&heap, 34);
  heap_insert(&heap, 15);
  heap_insert(&heap, 5);
  heap_insert(&heap, 12);
  heap_insert(&heap, 46);
  heap_insert(&heap, 19);
  heap_insert(&heap, 17);
  heap_insert(&heap, 11);
  heap_insert(&heap, 17);;

  heap_print(heap);

  /* get max */
  assert(heap_get_max(heap) == 46);

  return 0;
}
