typedef struct
{
  int vertex;
  int weight;
} edge_t;


typedef struct
{
  edge_t **edges;
  int edges_len;
  int edges_size;
  int visited;
  int distance;
  int prev;			// store the previous visited vertice
} vertex_t;

typedef struct
{
  vertex_t **vertices;
  int vertices_len;
  int vertices_size;
} graph_t;


/*
 * Add a vertex to the graph
 */
void graph_add_vertex(graph_t * g, int u);

/*
 * Add an edge to the graph, provided two vertices and one weight
 *
 * Args:
 * a, b: should be character in lowercase (e.g. 'a', 'b')
 */
void graph_add_edge(graph_t * g, int a, int b, int w);

/*
 * Print literal graph
 */
void graph_print(graph_t * g);

/*
 * Garbage collect the graph
 */
void graph_destroy();

/*
 * Print the path of Depth First Search from a source.
 */
void graph_dfs(graph_t *, int);


/*
 * Print the path of Breadth First Search from a source.
 */
void graph_bfs(graph_t *, int);


/*
 * Dijkstra's algorithm:
 * Only valid when all the weights are positive.
 * Print shortest path (of weights) between two vertices.
 * Returns the distance between two vertices.
 *
 */
int graph_dijkstra(graph_t *, int, int);


/*
 * Print the path to a vertice
 */
void graph_print_path(graph_t * q, int t);
