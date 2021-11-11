#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "bst.h"

#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(EXIT_FAILURE); }
#define check_addr(x) { if ((x) == NULL) panic("Unable to allocate memory"); }

static inline int
max(int a, int b)
{
  return a > b ? a : b;
}

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


int
bst_is_in(node_t * root, int key)
{
  if (root->val == key)
    return 1;
  if (!root || (!root->left && !root->right))
    return 0;

  if (root->val > key) {
    return bst_is_in(root->left, key);
  } else {
    return bst_is_in(root->right, key);
  }
}

int
bst_height(node_t * root)
{
  if (!root)
    return 0;
  return 1 + max(bst_height(root->left), bst_height(root->right));
}

node_t *
bst_min_node(node_t * root)
{
  if (!root || !root->left)
    return root;
  return bst_min_node(root->left);
}

node_t *
bst_max_node(node_t * root)
{
  if (!root || !root->right)
    return root;
  return bst_max_node(root->right);
}

/*
 * Ensure that the subtree doesn't hide a value that is
 * lower or larger than the root allows.
 */
int
is_between(node_t * root, int min_value, int max_value)
{
  if (!root)
    return 1;

  return min_value < root->val && root->val < max_value &&
    is_between(root->left, min_value, root->val) &&
    is_between(root->right, root->val, max_value);
}

int
is_bst(node_t * root)
{
  if (!root)
    return 1;

  return is_between(root, INT_MIN, INT_MAX);
}
