typedef struct queue queue_t;

/*
 * Create and return a pointer to a new queue
 */
queue_t *queue_new();

/*
 * Insert new item to queue (enqueue)
 */
void queue_put(queue_t *, int);

/*
 * Check if queue is empty
 */
int queue_is_empty(queue_t *);

/*
 * Get value at the top of the queue
 */
int queue_peek(queue_t *);

/*
 * Remove value at the top of the queue (dequeue)
 */
int queue_pop(queue_t *);

/*
 * Garbage collect the queue
 */
void queue_destroy(queue_t *);
