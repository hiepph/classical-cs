typedef struct node node_t;

/*
 * Create a new node with value.
 */
node_t *bst_new_node(int val);

/*
 * Insert a new nodw with new value into BST.
 * New node is inserted as a leaf node.
 * Ignore duplicated value.
 */
node_t *bst_insert(node_t * root, int val);

/*
 * Inorder print a tree (value from min->max).
 */
void bst_print_inorder(node_t * root);

/*
 * Check if a node is in tree.
 * Returns 1 if true, else 0.
 */
int bst_is_in(node_t * root, int key);

/*
 * Deallocate a bst.
 */
void bst_destroy(node_t * root);

/*
 * Get height of a BST
 */
int bst_height(node_t * root);


/*
 * Get node with the min value
 */
node_t *bst_min_node(node_t * root);

/*
 * Get node with the max value
 */
node_t *bst_max_node(node_t * root);


/*
 * Check if a bst
 */
int is_bst(node_t * root);

/*
 * Find a node in the tree with given value
 */
node_t *bst_find_node(node_t * root, int key);

/*
 * Find the next successor of a node
 * aka next larger value
 */
node_t *bst_successor_node(node_t * root, int key);

/*
 * Delete the node contain a value
 */
node_t *bst_delete(node_t * root, int key);
