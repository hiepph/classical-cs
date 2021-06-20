#include <stdio.h>

void
swap(int *a, int *b)
{
  int temp = *a;

  *a = *b;
  *b = temp;
}

/* ref: https://www.geeksforgeeks.org/bubble-sort/ */
void
bubble_sort(int *arr, int n)
{
  int i, j;

  /* optimized: break if no swap is executed */
  int swapped;

  for (i = 0; i < n - 1; i++) {
    swapped = 0;
    // last i elements are in place
    for (j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
	swap(&arr[j], &arr[j + 1]);
	swapped = 1;
      }
    }

    if (!swapped)
      break;
  }
}

int
main(void)
{
  int arr[] = { 4, 3, 2, 10, 12, 1, 5, 6 };
  int n = sizeof(arr) / sizeof(arr[0]);

  bubble_sort(arr, n);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
