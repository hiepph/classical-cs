#include <assert.h>

/*
 * N choose k
 * C(n, k) = C(n-1, k) + C(n-1, k-1)
 *        = #(1: choose element #c) + #(2: don't choose element #c)
 * 1: already choose #c -> choose another (k-1) elements
 *   from the remaining (n-1) elements
 * 2: choose k elements from the remaining (n-1) elements
 */
int
C(int n, int k)
{
  if (k == 0 || k == n)
    return 1;
  else
    return C(n-1, k-1) + C(n-1, k);
}

int
main()
{
  /* (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4) */
  assert(C(4, 3) == 4);
  return 0;
}
