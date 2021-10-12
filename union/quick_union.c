#include <stdio.h>
#define N 10000

/* trace the root of `cur` index */
int
root(const int *id, int cur)
{
  int i = cur;
  for (; i != id[i]; i = id[i])
    ;
  return i;
}

/* prints out not-yet-connected pairs */
main()
{
  int i, p, q, id[N];

  for (i = 0; i < N; i++) {
    id[i] = i;
  }

  while (scanf("%d %d\n", &p, &q) == 2) {
    int root_p = root(id, p);
    int root_q = root(id, q);

    if (root_p == root_q) continue;

    id[root_p] = root_q;

    printf("%d %d\n", p, q);
  }
}
