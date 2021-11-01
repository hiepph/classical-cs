/* ref: https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC */

#include <stdio.h>

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

/*
 * Do the partition by separating all the smaller elements to the left of
 * the pivot, and all the larger elements to the right of the pivot
 *
 * Pivot is chosen randomly for performance guarantee
 *
 * Return the index of the item now known to be in place
 */
int
partition(int *A, int l, int h)
{
  int i, j, pivot;

  pivot = l;
  i = l;
  j = h;

  while (1) {
    for (; i < h && A[i] < A[pivot]; ++i);
    for (; j > l && A[j] > A[pivot]; --j);

    if (i >= j) break;
    swap(&A[i], &A[j]);
  }

  swap(&A[pivot], &A[j]);

  return j;
}


void
quick_sort(int *A, int l, int h)
{
  if (l > h) return;
  int p = partition(A, l, h);
  quick_sort(A, l, p-1);
  quick_sort(A, p+1, h);
}


int main(void)
{
  int A[] = {4, 3, 2, 10, 12, 1, 5, 6};
  int n = sizeof(A) / sizeof(A[0]);

  quick_sort(A, 0, n - 1);
  for (int i = 0; i < n; ++i)
    printf("%d ", A[i]);
  putchar('\n');

  return 0;
}
