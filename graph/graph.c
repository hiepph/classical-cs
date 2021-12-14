#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

#define INITIAL_ARRAY_SIZE 4


/*
 * Each edge stores the destination vertex and weight
 */
void
graph_add_vertex(graph_t * g, int u)
{
  if (g->vertices_size < u + 1) {
    int new_size =
      (g->vertices_size * 2 > u) ?
      g->vertices_size * 2 : u + INITIAL_ARRAY_SIZE;

    g->vertices = realloc(g->vertices, new_size * sizeof(vertex_t *));
    for (int j = g->vertices_size; j < new_size; j++)
      g->vertices[j] = NULL;
    g->vertices_size = new_size;
  }

  if (!g->vertices[u]) {
    g->vertices[u] = calloc(1, sizeof(vertex_t));
    g->vertices_len++;
  }
}

/*
 * Each vertex stores a dynamic adjacency array of connected edges
 */
void
graph_add_edge(graph_t * g, int a, int b, int w)
{
  graph_add_vertex(g, a);
  graph_add_vertex(g, b);

  vertex_t *v = g->vertices[a];

  if (v->edges_len >= v->edges_size) {
    v->edges_size = v->edges_size ? v->edges_size * 2 : INITIAL_ARRAY_SIZE;
    v->edges = realloc(v->edges, v->edges_size * sizeof(edge_t *));
  }

  edge_t *e = calloc(1, sizeof(edge_t));

  e->vertex = b;
  e->weight = w;

  v->edges[v->edges_len++] = e;
}

void
graph_print(graph_t * g)
{
  for (int i = 0; i < g->vertices_len; i++) {
    vertex_t *u = g->vertices[i];

    if (u) {
      for (int j = 0; j < u->edges_len; j++) {
	if (u->edges[j]) {
	  printf("%d --> %d (%d)\n",
		 i, u->edges[j]->vertex, u->edges[j]->weight);
	}
      }
    }
  }
}


void
graph_destroy(graph_t * g)
{
  for (int i = 0; i < g->vertices_len; i++) {
    vertex_t *v = g->vertices[i];

    if (v) {
      for (int j = 0; j < v->edges_len; j++) {
	if (v->edges[j])
	  free(v->edges[j]);
      }
      free(v);
    }
  }

  free(g);
}


/*
 * Recursive DFS.
 * We keep track of the path travelled and the number of visited vertices.
 */
void
dfs_recur(graph_t * g, int s, int *path, int *count)
{
  vertex_t *u = g->vertices[s];
  vertex_t *v;

  u->visited = 1;
  for (int j = 0; j < u->edges_len; j++) {
    int d = u->edges[j]->vertex;

    v = g->vertices[d];
    if (!v->visited) {
      dfs_recur(g, d, path, count);
    }
  }

  path[(*count)++] = s;
}

/*
 * Reverse a given array
 */
void
reverse_array(int *A, int n)
{
  if (n == 1)
    return;

  for (int i = 0; i < n / 2; i++) {
    int temp = A[i];

    A[i] = A[n - 1 - i];
    A[n - 1 - i] = temp;
  }
}

void
graph_dfs(graph_t * g, int s)
{
  int *path = malloc(g->vertices_len * sizeof(int));
  int count = 0;

  dfs_recur(g, s, path, &count);

  reverse_array(path, count);
  for (int i = 0; i < count; i++) {
    printf("%d ", path[i]);
  }
  free(path);
}
