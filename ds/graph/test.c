#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "graph.h"

int
main()
{
  graph_t *g = calloc(1, sizeof(graph_t));
  int dist;

  printf("Graph:\n");
  graph_add_edge(g, 0, 1, 7);
  graph_add_edge(g, 0, 2, 9);
  graph_add_edge(g, 0, 5, 14);
  graph_add_edge(g, 1, 2, 10);
  graph_add_edge(g, 1, 3, 15);
  graph_add_edge(g, 2, 3, 11);
  graph_add_edge(g, 2, 5, 2);
  graph_add_edge(g, 3, 4, 6);
  graph_add_edge(g, 4, 5, 9);
  graph_print(g);

  printf("DFS from 0:\n");
  graph_dfs(g, 0);

  printf("BFS from 0:\n");
  graph_bfs(g, 0);

  dist = graph_dijkstra(g, 0, 4);
  printf("(Dijkstra) Distance from 0 -> 4: %d. Path: ", dist);
  graph_print_path(g, 4);
  assert(dist == 26);

  dist = graph_dijkstra(g, 0, 5);
  printf("(Dijkstra) Distance from 0 -> 5: %d. Path: ", dist);
  graph_print_path(g, 5);
  assert(dist == 11);

  graph_destroy(g);
  return 0;
}
