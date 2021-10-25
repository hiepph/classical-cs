#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(EXIT_FAILURE); }

struct node
{
  int value;
  struct node *next;
};


void
check_addr(node_t * head)
{
  if (head == NULL) {
    panic("Unable to allocate memory\n");
  }
}

int
l_size(node_t * head)
{
  node_t *cur = head;
  int cnt = 0;

  while (cur != NULL) {
    cur = cur->next;
    cnt++;
  }

  return cnt;
}

int
l_is_empty(node_t * head)
{
  return head == NULL;
}

int
l_value_at(node_t * head, int idx)
{
  node_t *cur = head;
  int i = 0;

  while (cur != NULL && i < idx) {
    cur = cur->next;
    i++;
  }

  if (i < idx) {
    panic("Index out of bound");
  }

  return cur->value;
}

void
l_destroy(node_t * head)
{
  node_t *temp;

  while (head != NULL) {
    temp = head->next;
    free(head);
    head = temp;
  }
}

node_t *
l_new_node(int val)
{
  node_t *new_node = malloc(sizeof(node_t));

  check_addr(new_node);
  new_node->value = val;
  new_node->next = NULL;
  return new_node;
}

node_t *
l_push_front(node_t * head, int value)
{
  node_t *new_node = l_new_node(value);

  if (head == NULL) {
    return new_node;
  }

  new_node->next = head;
  head = new_node;
  return head;
}

int
l_pop_front(node_t ** head)
{
  int val = (*head)->value;
  node_t *temp = *head;

  (*head) = (*head)->next;
  free(temp);

  return val;
}

node_t *
l_push_back(node_t * head, int val)
{
  node_t *cur = head;
  node_t *new_node = l_new_node(val);

  if (head == NULL) {
    return new_node;
  }

  while (cur->next != NULL) {
    cur = cur->next;
  }
  cur->next = new_node;

  return head;
}

int
l_pop_back(node_t ** head)
{
  if (*head == NULL) {
    panic("List is empty");
  }

  int val;
  node_t *cur = *head;
  node_t *prev = NULL;

  while (cur->next != NULL) {
    prev = cur;
    cur = cur->next;
  }

  if (prev != NULL) {
    prev->next = NULL;
  } else {
    *head = NULL;
  }

  val = cur->value;
  free(cur);

  return val;
}

node_t *
l_insert_at(node_t * head, int idx, int value)
{
  if (idx == 0) {
    return l_push_front(head, value);
  }

  node_t *new_node = l_new_node(value);
  node_t *cur = head;
  int i = 1;

  while (cur->next && i < idx) {
    cur = cur->next;
    i++;
  }
  if (i < idx) {
    panic("Index out of bound");
  }

  new_node->next = cur->next;
  cur->next = new_node;

  return head;
}

node_t *
l_delete_at(node_t * head, int idx)
{
  if (head == NULL) {
    panic("List is empty");
  }

  int val;
  int i = 0;
  node_t *cur = head;
  node_t *prev = NULL;

  while (cur->next != NULL && i < idx) {
    prev = cur;
    cur = cur->next;
    i++;
  }
  if (i < idx) {
    panic("Index out of bound");
  }

  if (prev != NULL) {
    prev->next = cur->next;
  } else {
    head = NULL;
  }

  free(cur);

  return head;
}
