/* #include <std */
#include "binary_search.h"

int
binary_search(int target, const int *a, size_t length)
{
  size_t index;

  index = length / 2;

  if (length == 0) {
    return 0;
  } else if (target == a[index]) {
    return 1;
  } else if (target < a[index]) {
    /* bottom half */
    return binary_search(target, a, index);
  } else {
    /* top half */
    return binary_search(target, a+index+1, length - (index + 1));
  }
}
