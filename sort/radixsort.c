#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void
counting_sort(int *arr, int n, int exp)
{
  int i;
  int k = 10;			// base 10
  int *count, *sorted;

  /* initialize the count array with 0 values */
  count = malloc(sizeof(int) * k);
  assert(count);
  for (i = 0; i < k; i++) {
    count[i] = 0;
  }

  /* endorse the count with the index from the array */
  /* Note we only extract the current exp digit */
  for (i = 0; i < n; i++) {
    count[(arr[i] / exp) % 10]++;
  }

  /* calculate the rolling sum */
  for (i = 1; i < k; i++) {
    count[i] += count[i - 1];
  }

  /* Create an array, and move the corresponding element to
     right place according to the count array */
  sorted = malloc(sizeof(arr));
  assert(sorted);
  /* Note: we loop inversely because we want to keep the position order */
  for (i = n - 1; i >= 0; i--) {
    sorted[count[(arr[i] / exp) % 10] - 1] = arr[i];
    count[(arr[i] / exp) % 10]--;
  }

  /* copy back the value to the original array */
  for (i = 0; i < n; i++) {
    arr[i] = sorted[i];
  }

  free(sorted);
  free(count);
}

/* ref: https://www.geeksforgeeks.org/radix-sort/ */
void
radix_sort(int *arr, int n, int k)
{
  int max;
  int i, exp;

  /* count the number of digits of the maximum number */
  max = arr[0];
  for (i = 1; i < n; i++) {
    if (max < arr[i]) {
      max = arr[i];
    }
  }

  /* do counting sort for every digit */
  /* starting from the lowest */
  for (exp = 1; exp < max; exp *= 10) {
    counting_sort(arr, n, exp);
  }
}

int
main(void)
{
  int arr[] = { 170, 45, 75, 90, 802, 24, 2, 66 };
  int n = sizeof(arr) / sizeof(arr[0]);
  int k = 10;

  radix_sort(arr, n, k);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
