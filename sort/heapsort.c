#include <stdio.h>

void
swap(int *a, int *b)
{
  int temp = *a;

  *a = *b;
  *b = temp;
}

void
sift_down(int *A, int n, int idx)
{
  int max_idx = idx;
  int l = 2 * idx + 1;
  int r = 2 * idx + 2;

  if (l < n && A[l] > A[max_idx])
    max_idx = l;
  if (r < n && A[r] > A[max_idx])
    max_idx = r;

  if (idx != max_idx) {
    swap(&A[idx], &A[max_idx]);
    sift_down(A, n, max_idx);
  }
}

void
heapify(int *A, int n)
{
  for (int i = n / 2; i >= 0; i--) {
    sift_down(A, n, i);
  }
}

void
heap_sort(int *A, int n)
{
  heapify(A, n);
  int size = n;

  while (size > 1) {
    swap(&A[0], &A[size - 1]);
    size--;
    sift_down(A, size, 0);
  }
}


int
main(void)
{
  int A[] = { 4, 3, 2, 10, 12, 1, 5, 6 };
  int n = sizeof(A) / sizeof(A[0]);

  heap_sort(A, n);
  for (int i = 0; i < n; ++i)
    printf("%d ", A[i]);
  putchar('\n');

  return 0;
}
