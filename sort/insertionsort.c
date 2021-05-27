#include <stdio.h>

void insertion_sort(int *arr, int n)
{
  for (int i = 1; i < n; ++i) {
    // shift the precedent list to the right
    // insert the current element to the right position
    // e.g.: 1 3 4 2 ... -> 1 2 3 4 ...
    int j;
    int cur =  arr[i];
    for (j = i-1; j >= 0 && arr[j] > cur; --j)
      arr[j + 1] = arr[j];
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
