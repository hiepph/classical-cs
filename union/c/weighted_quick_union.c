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
  int i, p, q, id[N], sz[N];

  for (i = 0; i < N; i++) {
    id[i] = i;
    sz[i] = 1;
  }

  while (scanf("%d %d\n", &p, &q) == 2) {
    int root_p = root(id, p);
    int root_q = root(id, q);

    if (root_p == root_q) continue;

    if (sz[root_p] < sz[root_q]) {
      id[root_p] = root_q;
      sz[root_q] += sz[root_p];
    } else {
      id[root_q] = root_p;
      sz[root_p] += sz[root_q];
    }

    printf("%d %d\n", p, q);
  }
}
