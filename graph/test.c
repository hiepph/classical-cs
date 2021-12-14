#include <stdlib.h>
#include "graph.h"

int
main()
{
  graph_t *g = calloc(1, sizeof(graph_t));

  graph_add_edge(g, 'a', 'b', 7);

  graph_destroy(g);
  return 0;
}
