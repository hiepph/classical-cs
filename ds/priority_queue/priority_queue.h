typedef struct heap heap_t;
typedef struct node node_t;


heap_t *heap_new();

void heap_destroy(heap_t *);

/*
 * Insert/update a value with priority
 */
void heap_put(heap_t *h, int priority, int val);

/*
 * Pop an element with the highest priority and return its value
 */
int heap_pop(heap_t *);
