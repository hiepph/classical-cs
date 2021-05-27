#include <stdio.h>

// ref: https://www.geeksforgeeks.org/insertion-sort/
void insertion_sort(int *arr, int n)
{
  int i, j;
  int cur;

  for (i = 1; i < n; ++i) {
    cur =  arr[i];
    // shift the precedent list to the right
    for (j = i-1; j >= 0 && arr[j] > cur; --j) {
      arr[j + 1] = arr[j];
    }
    // insert the current element to the right position
    // e.g.: 1 3 4 (2) ... -> 1 (2) 3 4 ...
    arr[j+1] = cur;
  }
}

int main(void)
{
  int arr[] = {4, 3, 2, 10, 12, 1, 5, 6};
  int n = sizeof(arr) / sizeof(arr[0]);

  insertion_sort(arr, n);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n');

  return 0;
}
