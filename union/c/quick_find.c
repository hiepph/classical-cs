#include <stdio.h>
#define N 10000

/* prints out not-yet-connected pairs */
main()
{
  int i, p, q, id[N];

  for (i = 0; i < N; i++) {
    id[i] = i;
  }

  while (scanf("%d %d\n", &p, &q) == 2) {
    if (id[p] == id[q]) {
      continue;
    }

    int temp = id[p];
    for (i = 0; i < N; i++) {
      if (id[i] == temp) {
        id[i] = id[q];
      }
    }

    printf("%d %d\n", p, q);
  }
}
