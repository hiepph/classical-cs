typedef struct node node_t;

void new_node(int);

/* check the allocation of memory */
void check_addr(node_t *);

/* Returns the number of nodes in the list */
int l_size(node_t *);

/* Free the memory of the list */
void l_destroy(node_t *);


/*
 * Check if the list is empty
 * Returns 1 if true, 0 o.w
 */
int l_is_empty(node_t * head);


/*
 * Return the value at index
 */
int l_value_at(node_t * head, int idx);

/*
 * Create a new node
 */
node_t *l_new_node(int val);


/*
 * Adds an item to the front of the list
 */
node_t *l_push_front(node_t * head, int value);


/*
 * Pop the item at the front and return its value
 */
int l_pop_front(node_t ** head);

/*
 * Push an item at the back of the list
 */
node_t *l_push_back(node_t * head, int val);

/*
 * Pop the item at the back and return its value
 */
int l_pop_back(node_t ** head);


/*
 * Insert a value in the list at a given index
 */
node_t *l_insert_at(node_t * head, int idx, int value);


/*
 * Delete a node at a given index
 */
node_t *l_delete_at(node_t * head, int idx);
