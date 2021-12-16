#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "graph.h"
#include "queue.h"
#include "priority_queue.h"


#define panic(msg, ...) { \
    fprintf(stderr, "ERROR: %s", (msg), ##__VA_ARGS__); \
    exit(1); \
  }
#define check_addr(x) { if ((x) == NULL) panic("Unable to allocate memory"); }

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

/*
 * Reset vertices' visited and distant state
 */
void
reset_vertices(graph_t * g)
{
  for (int i = 0; i < g->vertices_len; i++) {
    g->vertices[i]->visited = 0;
    g->vertices[i]->distance = -1;
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
  printf("\n");

  reset_vertices(g);
  free(path);
}


void
graph_bfs(graph_t * g, int s)
{
  queue_t *q;
  int *path;
  int count;
  vertex_t *u, *v;

  path = malloc(g->vertices_len * sizeof(int));
  count = 0;

  q = queue_new();
  queue_put(q, s);
  g->vertices[s]->visited = 1;
  path[count++] = s;

  check_addr(path);
  while (!queue_is_empty(q)) {
    u = g->vertices[queue_pop(q)];
    for (int j = 0; j < u->edges_len; j++) {
      int v_val = u->edges[j]->vertex;

      v = g->vertices[v_val];
      if (!v->visited) {
	queue_put(q, v_val);
	path[count++] = v_val;
	v->visited = 1;
      }
    }
  }

  for (int i = 0; i < count; i++) {
    printf("%d ", path[i]);
  }
  printf("\n");

  reset_vertices(g);
  free(path);
  queue_destroy(q);
}

int
graph_dijkstra(graph_t * g, int s, int t)
{
  heap_t *q;
  vertex_t *u, *v;
  int distance;

  for (int i = 0; i < g->vertices_len; i++) {
    g->vertices[i]->distance = INT_MAX;
  }
  g->vertices[s]->distance = 0;

  q = heap_new();
  for (int i = 0; i < g->vertices_len; i++) {
    heap_put(q, g->vertices[i]->distance, i);
  }

  while (!heap_is_empty(q)) {
    int u_val = heap_pop(q);

    u = g->vertices[u_val];
    for (int j = 0; j < u->edges_len; j++) {
      int v_val = u->edges[j]->vertex;

      v = g->vertices[v_val];
      if (v->distance > (u->distance + u->edges[j]->weight)) {
	v->distance = u->distance + u->edges[j]->weight;
	heap_put(q, v->distance, v_val);
      }
    }
  }

  heap_destroy(q);

  v = g->vertices[t];
  distance = v->distance == INT_MAX ? -1 : v->distance;

  reset_vertices(g);

  return distance;
}
