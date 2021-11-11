#include <assert.h>
#include "bst.c"
#include "bst.h"

int
main(void)
{
  node_t *root = NULL;

  /* insertion */
  root = bst_insert(root, 4);
  assert(root->val == 4);

  root = bst_insert(root, 12);
  root = bst_insert(root, 3);
  root = bst_insert(root, 11);
  root = bst_insert(root, 16);

  /* print */
  printf("Inorder print: ");
  bst_print_inorder(root);
  printf("\n");

  /* find */
  assert(bst_is_in(root, 12));
  assert(bst_is_in(root, 3));
  assert(!bst_is_in(root, 9));

  /* height */
  assert(bst_height(root) == 3);

  /* min, max node */
  assert(bst_min_node(root)->val == 3);
  assert(bst_max_node(root)->val == 16);

  /* bst? */
  assert(is_bst(root));

  bst_destroy(root);
  return 0;
}
