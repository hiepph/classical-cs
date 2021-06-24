#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void
merge(int *arr, int l, int m, int r)
{
  int i, j, k;
  int *L, *R;
  int nL = m - l + 1;
  int nR = r - m;

  /* create temp arrays for storing 2 halves */
  L = malloc(sizeof(int) * nL);
  R = malloc(sizeof(int) * nR);
  assert(L);
  assert(R);

  for (i = 0; i < nL; i++) {
    L[i] = arr[l + i];
  }
  for (j = 0; j < nR; j++) {
    R[j] = arr[m + 1 + j];
  }

  k = l;			// initial index of the original array
  i = 0;			// initial index of L
  j = 0;			// initial index of R
  while (i < nL && j < nR) {
    if (L[i] < R[j]) {
      arr[k] = L[i];
      i++;
    }
    else {
      arr[k] = R[j];
      j++;
    }

    k++;
  }

  /* copy the remaining elements */
  while (i < nL) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < nR) {
    arr[k] = R[j];
    j++;
    k++;
  }

  free(L);
  free(R);
}

void
merge_sort(int *arr, int l, int r)
{
  int m;

  if (l < r) {
    m = l + (r - l) / 2;	// avoid overflow

    /* sort 2 halves and join */
    merge_sort(arr, l, m);
    merge_sort(arr, m + 1, r);

    merge(arr, l, m, r);
  }
}

int
main(void)
{
  int arr[] = { 2, 4, 3, 1, 3, 5, 4, 2, 4, 5, 3, 9, 8 };
  int n = sizeof(arr) / sizeof(arr[0]);

  merge_sort(arr, 0, n - 1);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
