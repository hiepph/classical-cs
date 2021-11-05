#include <stdio.h>
#include <stdlib.h>
#include "bst.h"

#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(EXIT_FAILURE); }
#define check_addr(x) { if ((x) == NULL) panic("Unable to allocate memory"); }

struct node
{
  int val;
  struct node *left;
  struct node *right;
};


node_t *
bst_new_node(int val)
{
  node_t *new_node = malloc(sizeof(node_t));

  check_addr(new_node);
  new_node->val = val;
  new_node->left = NULL;
  new_node->right = NULL;
  return new_node;
}

void
bst_print_inorder(node_t * root)
{
  if (root->left)
    bst_print_inorder(root->left);
  if (root) {
    printf("%d ", root->val);
  }
  if (root->right)
    bst_print_inorder(root->right);
}

void
bst_destroy(node_t * root)
{
  if (root) {
    bst_destroy(root->left);
    bst_destroy(root->right);
    free(root);
  };
}


node_t *
bst_insert(node_t * root, int val)
{
  if (!root) {
    root = bst_new_node(val);
    return root;
  }

  if (root->val == val) {
    return root;
  }

  if (root->val > val) {
    root->left = bst_insert(root->left, val);
  } else {
    root->right = bst_insert(root->right, val);
  }

  return root;
}
