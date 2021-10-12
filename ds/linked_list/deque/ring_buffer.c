// implementatin of deque with ring buffer
// ref: https://cs.yale.edu/homes/aspnes/classes/223/notes.html#ringBuffers
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

#include "deque.h"

struct deque {
  size_t base; // location of front element
  size_t length; // length of region in use
  size_t size; // number of positions in content
  int *contents;
};

#define INITIAL_SIZE (8)

Deque* deque_new_with_size(size_t size)
{
  struct deque *d;

  d = malloc(sizeof(struct deque));
  assert(d);

  d->base = 0;
  d->length = 0;
  d->size = INITIAL_SIZE;

  d->contents = malloc(sizeof(int) * d->size);
  assert(d->contents);

  return d;
}

Deque* deque_new(void) {
  return deque_new_with_size(INITIAL_SIZE);
}

int deque_empty(const Deque* d)
{
  return d->length == 0;
}

void deque_destroy(Deque *d)
{
  free(d->contents);
  free(d);
}

void deque_push(Deque* d, int direction, int value)
{
  struct deque *d_new;
  int *old_contents;

  /* if (d->length == d->size) { */
  /*   // no space to add more elements */
  /*   // allocate a new deque with double size */
  /*   d_new = deque_new_with_size(d->size * 2); */

  /*   // migrate d -> d_new */
  /*   while (!deque_empty(d)) { */
  /*     deque_push(d_new, DEQUE_BACK, deque_pop(d, DEQUE_FRONT)); */
  /*   } */

  /*   // repoint d -> d_new */
  /*   // delete old contents */
  /*   old_contents = d->contents; */
  /*   *d = *d_new; */

  /*   free(old_contents); */
  /*   free(d_new); */
  /* } */

  // (b) | | | ... | | (f)
  if (direction == DEQUE_FRONT) {
    // example: PUSH 1; PUSH 2; PUSH 3
    // (b) | ... | 3 | 2 | 1 | (f)
    //            base     |
    //                  contents[base]
    // switch the base to the front
    if (d->base == 0) {
      d->base = d->size-1;
    } else {
      d->base--;
    }

    d->length++;
    d->contents[d->base] = value;
  } else {
    // example: PUSH 1; PUSH 2; PUSH 3
    // (b) | 3 | 2 | 1 | ... | (f)
    //      base
    //       |
    //     contents[base]
    d->contents[(d->base + d->length++) % d->size] = value;
  }
}

int deque_pop(Deque* d, int direction)
{
  int v;

  if (deque_empty(d)) {
    return DEQUE_EMPTY;
  }

  if (direction == DEQUE_FRONT) {
    v = d->contents[d->base];

    d->base = (d->base + 1) % d->size;
    d->length--;
  } else {
    v = d->contents[(d->base + --d->length) % d->size];
  }

  return v;
}

int main(int argc, char **argv)
{
  int i;
  int n;
  Deque *d;

  if(argc != 2) {
    fprintf(stderr, "Usage: %s iterations\n", argv[0]);
    return 1;
  }
  n = atoi(argv[1]);

  d = deque_new();
  assert(deque_empty(d));

  for(i = 0; i < n; i++) {
      deque_push(d, DEQUE_FRONT, i);
      assert(!deque_empty(d));
  }

  for(i = 0; i < n; i++) {
      assert(deque_pop(d, DEQUE_BACK) == i);
  }

  assert(deque_empty(d));

  for(i = 0; i < n; i++) {
      deque_push(d, DEQUE_BACK, i);
      assert(!deque_empty(d));
  }

  for(i = 0; i < n; i++) {
      assert(deque_pop(d, DEQUE_FRONT) == i);
  }

  assert(deque_empty(d));

  for(i = 0; i < n; i++) {
      deque_push(d, DEQUE_BACK, i);
      assert(!deque_empty(d));
  }

  for(i = n-1; i >= 0; i--) {
      assert(deque_pop(d, DEQUE_BACK) == i);
  }

  assert(deque_empty(d));

  for(i = 0; i < n; i++) {
      deque_push(d, DEQUE_FRONT, i);
  }

  for(i = n-1; i >= 0; i--) {
      assert(deque_pop(d, DEQUE_FRONT) == i);
  }

  assert(deque_empty(d));

  assert(deque_pop(d, DEQUE_FRONT) == DEQUE_EMPTY);

  assert(deque_pop(d, DEQUE_BACK) == DEQUE_EMPTY);

  deque_push(d, DEQUE_FRONT, 12);

  deque_destroy(d);

  return 0;
}
