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

  /* find */
  root = bst_insert(root, 5);
  assert(bst_find_node(root, 10) == NULL);
  assert(bst_find_node(root, 3)->val == 3);
  assert(bst_find_node(root, 11)->val == 11);
  assert(bst_find_node(root, 12)->val == 12);

  /* successor */
  assert(bst_successor_node(root, 4)->val == 5);
  assert(bst_successor_node(root, 12)->val == 16);

  /* delete */
  printf("Tree: ");
  bst_print_inorder(root);
  printf("\n");

  printf("Delete 3: ");
  root = bst_delete_value(root, 3);
  assert(!bst_is_in(root, 3));
  bst_print_inorder(root);
  printf("\n");

  printf("Delete 11: ");
  root = bst_delete_value(root, 11);
  assert(!bst_is_in(root, 11));
  bst_print_inorder(root);
  printf("\n");

  printf("Delete 12: ");
  root = bst_delete_value(root, 12);
  assert(!bst_is_in(root, 12));
  bst_print_inorder(root);
  printf("\n");

  bst_destroy(root);
  return 0;
}
