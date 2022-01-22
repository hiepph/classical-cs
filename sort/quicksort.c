#include <stdio.h>
#include <stdlib.h>

void swap(int *A, int a, int b)
{
  int temp = A[a];
  A[a] = A[b];
  A[b] = temp;
}

/*
 * Do the partition by separating all the smaller elements to the left of
 * the pivot, and all the larger elements to the right of the pivot.
 *
 * Pivot is chosen default as the first (left-most) element.
 * The left index will try to find all larger elements,
 * while the right index will try to find all smaller elements.
 * Swap those 2 pointers continually.
 * Finally swap the pivot pointer to achieve the goal.
 *
 * Return the index of the item now known to be in place
 */
int
partition(int *A, int l, int h)
{
  int i, j, p;

  p = l;
  i = l;
  j = h+1;

  while (1) {
    while (A[++i] < A[p])
      if (i == h)
        break;

    while (A[p] < A[--j])
      if (j == l)
        break;

    if (i >= j) break;
    swap(A, i, j);
  }

  swap(A, p, j);

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


/*
 *
 * Pivot is chosen randomly for performance guarantee
 * (not reaching the worst case which is O(n^2))
 */
int
generate_random_number_in_range(int min, int max)
{
  return min + rand() % (max - min + 1);
}

int
parititon_random_pivot(int *A, int l, int h)
{

}

void
quick_sort_random_pivot(int *A, int l, int h)
{

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
