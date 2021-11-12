#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"

#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(1); }


struct node
{
  char *key;
  int value;
};

struct hash_table
{
  struct node **data;
  int size;
};

hash_table_t *
hash_table_create(const int size)
{
  hash_table_t *new_table = malloc(sizeof(hash_table_t));

  if (new_table == NULL) {
    panic("Allocate memory for a new table.");
  }

  new_table->data = malloc(sizeof(node_t) * size);
  if (new_table->data == NULL) {
    panic("Allocate memory for data of the new table.");
  }
  new_table->size = size;

  for (int i = 0; i < size; i++) {
    new_table->data[i] = NULL;
  }

  return new_table;
}

void
hash_table_destroy(hash_table_t * table)
{
  for (int i = 0; i < table->size; i++) {
    if (table->data[i]) {
      // TODO: free key
    }
  }
  free(table->data);
  free(table);
}
