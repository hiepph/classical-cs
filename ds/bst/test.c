#include <assert.h>
#include "bst.c"
#include "bst.h"

int
main(void)
{
  node_t *root = NULL;

  /* bst_insert */
  root = bst_insert(root, 4);
  assert(root->val == 4);

  root = bst_insert(root, 12);
  root = bst_insert(root, 3);
  root = bst_insert(root, 11);
  root = bst_insert(root, 16);

  bst_print_inorder(root);
  puts("\n");

  bst_destroy(root);
  return 0;
}
