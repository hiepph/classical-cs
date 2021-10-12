typedef struct node node_t;

void new_node(int);

/* check the allocation of memory */
void
check_addr(node_t *);

/* Returns the number of nodes in the list */
int l_size(node_t *);

/* Free the memory of the list */
void l_destroy(node_t *);
