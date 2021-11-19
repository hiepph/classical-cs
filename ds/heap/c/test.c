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

  printf("Original: ");
  heap_print(heap);

  /* get size */
  assert(heap_get_size(heap) == 11);

  /* get max */
  assert(heap_get_max(heap) == 46);

  /* extract max */
  assert(heap_extract_max(&heap) == 46);
  printf("Extract max: ");
  heap_print(heap);
  assert(heap_get_size(heap) == 10);
  assert(heap_get_max(heap) == 34);

  assert(heap_extract_max(&heap) == 34);
  printf("Extract max: ");
  heap_print(heap);
  assert(heap_get_size(heap) == 9);
  assert(heap_get_max(heap) == 19);

  return 0;
}
