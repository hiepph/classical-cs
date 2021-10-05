#include "binary_search.h"

int
binary_search(int target, const int *a, size_t length)
{
  size_t index;

  for (;;) {
    index = length / 2;

    if (length == 0) {
      return 0;
    } else if (target == a[index]) {
      return 1;
    } else if (target < a[index]) {
      /* bottom half */
      length = index;
    } else {
      /* top half */
      a = a + index + 1;
      length = length - (index + 1);
    }
  }
}
