typedef struct max_heap max_heap_t;

/*
 * Define a new heap
 */
max_heap_t heap_new(int capacity);

/*
 * Insert a new value into heap
 */
void heap_insert(max_heap_t * heap, int value);

/*
 * The number of elements stored
 */
int heap_get_size(max_heap_t heap);

/*
 * Get max value
 */
int heap_get_max(max_heap_t heap);

/*
 * Get max value, and remove it
 */
int heap_extract_max(max_heap_t * heap);


/*
 * Remove an item at a given index
 */
void heap_remove(max_heap_t * heap, int idx);
