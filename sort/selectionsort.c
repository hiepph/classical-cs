#include <stdio.h>

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

// ref: https://www.geeksforgeeks.org/selection-sort/
void selection_sort(int *arr, int n)
{
  int i, j;
  int min_idx;

  for (i = 0; i < n-1; ++i) {
    min_idx = i;
    for (j = i+1; j < n; ++j) {
      // find the smaller element than the current index
      if (arr[j] < arr[min_idx]) {
        min_idx = j;
      }
    }

    // swap two values
    swap(&arr[i], &arr[min_idx]);
  }
}

int main(void)
{
  int arr[] = {4, 3, 2, 10, 12, 1, 5, 6};
  int n = sizeof(arr) / sizeof(arr[0]);

  selection_sort(arr, n);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
