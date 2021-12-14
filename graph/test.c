#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

int
main()
{
  graph_t *g = calloc(1, sizeof(graph_t));

  printf("Graph:\n");
  graph_add_edge(g, 'a', 'b', 7);
  graph_add_edge(g, 'a', 'c', 9);
  graph_add_edge(g, 'a', 'f', 14);
  graph_add_edge(g, 'b', 'c', 10);
  graph_add_edge(g, 'b', 'd', 15);
  graph_add_edge(g, 'c', 'd', 11);
  graph_add_edge(g, 'c', 'f', 2);
  graph_add_edge(g, 'd', 'e', 6);
  graph_add_edge(g, 'e', 'f', 9);

  graph_print(g);
  graph_destroy(g);
  return 0;
}
