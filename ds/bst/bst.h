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
 * Deallocate a bst.
 */
void bst_destroy(node_t * root);
