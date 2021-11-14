typedef struct max_heap max_heap_t;

/*
 * Define a new heap
 */
max_heap_t heap_new(int capacity);

/*
 * Insert a new value into heap
 */
void heap_insert(max_heap_t * heap, int value);
