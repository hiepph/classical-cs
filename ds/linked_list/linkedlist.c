#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

struct node
{
  int value;
  struct node *next;
};


void
check_addr(node_t *head)
{
  if (head == NULL) {
    printf("Unable to allocate memory\n");
    exit(EXIT_FAILURE);
  }
}

int l_size(node_t * head)
{
  node_t *cur = head;
  int cnt = 0;

  while (cur != NULL) {
    cur = cur->next;
    cnt++;
  }

  return cnt;
}

void
l_destroy(node_t *head)
{
  node_t *temp = head;
  while (head != NULL) {
    temp = head->next;
    free(head);
    head = head->next;
  }
}
