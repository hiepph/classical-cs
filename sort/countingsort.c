#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* ref:
   https://www.youtube.com/watch?v=1mh2vilbZMg
   https://www.geeksforgeeks.org/counting-sort */
void
counting_sort(int *arr, int n, int k)
{
  int i;
  int *count, *sorted;

  /* initialize the count array with 0 values */
  count = malloc(sizeof(int) * k);
  assert(count);
  for (i = 0; i < k; i++) {
    count[i] = 0;
  }

  /* endorse the count with the index from the array */
  for (i = 0; i < n; i++) {
    count[arr[i]]++;
  }

  /* calculate the rolling sum */
  for (i = 1; i < k; i++) {
    count[i] += count[i - 1];
  }

  /* Create an array, and move the corresponding element to
     right place according to the count array */
  sorted = malloc(sizeof(arr));
  assert(sorted);
  for (i = 0; i < n; i++) {
    sorted[count[arr[i]] - 1] = arr[i];
    count[arr[i]]--;
  }

  /* copy back the value to the original array */
  for (i = 0; i < n; i++) {
    arr[i] = sorted[i];
  }

  free(sorted);
  free(count);
}

int
main(void)
{
  int arr[] = { 2, 4, 3, 1, 3, 5, 4, 2, 4, 5, 3, 9, 8 };
  int n = sizeof(arr) / sizeof(arr[0]);
  int k = 10;

  counting_sort(arr, n, k);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
