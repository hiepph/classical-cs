#include <stdio.h>

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

void shell_sort(int *arr, int n)
{
  int gap;
  int temp;
  int i, j;

  /* start with a big gap, and then gradually reduce the gap */
  /* do insertion sort with gap step */
  for (gap = n / 2; gap > 0; gap /= 2) {
    for (i = gap; i < n; i++) {
      temp = arr[i];

      /* shift the elements to the right with gap step */
      for (j = i-gap; j >= 0 && arr[j] > temp; j -= gap) {
        arr[j + gap] = arr[j];
      }

      /* insert the element to the right position */
      arr[j+gap] = temp;
    }
  }
}

int main(void)
{
  int arr[] = {4, 3, 2, 10, 12, 1, 5, 6};
  int n = sizeof(arr) / sizeof(arr[0]);

  shell_sort(arr, n);
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  putchar('\n'); return 0;
}
