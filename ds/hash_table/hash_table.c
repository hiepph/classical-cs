#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hash_table.h"

#define panic(msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(1); }

struct node
{
  char *key;
  int value;
  struct node *next;
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
  node_t *temp;

  for (int i = 0; i < table->size; i++) {
    if (table->data[i]) {
      while (table->data[i]) {
	temp = table->data[i]->next;
	free(table->data[i]->key);
	free(table->data[i]);
	table->data[i] = temp;
      }
      free(table->data[i]);
    }
  }
  free(table->data);
  free(table);
}

/*
 * Polynomial hash
 */
int
hash(char *key)
{
  int multiplier = 263;
  unsigned int big_prime = 1000000007;
  int n = strlen(key);
  int hash = 0;

  for (int i = n - 1; i >= 0; i--) {
    hash = (hash * multiplier + key[i]) % big_prime;
  }

  return hash;
}

node_t *
hash_table_get_node(hash_table_t * table, char *key)
{
  int index = hash(key) % table->size;

  if (!table->data[index])
    return NULL;

  node_t *cur = table->data[index];

  while (cur) {
    if (strcmp(cur->key, key) == 0) {
      return cur;
    }
    cur = cur->next;
  }

  return NULL;
}

void
hash_table_add(hash_table_t * table, char *key, int value)
{
  int index = hash(key) % table->size;
  node_t *node = hash_table_get_node(table, key);

  if (node != NULL) {
    node->value = value;
    return;
  }

  node = malloc(sizeof(node_t));
  if (node == NULL) {
    panic("Allocate memory for a (key-value).");
  }
  node->key = strdup(key);
  node->value = value;
  node->next = NULL;
  if (table->data[index]) {
    table->data[index]->next = node;
  } else {
    table->data[index] = node;
  }
}

int
hash_table_get(hash_table_t * table, char *key)
{
  node_t *node = hash_table_get_node(table, key);

  if (!node)
    return NULL;
  return node->value;
}

int
hash_table_is_in(hash_table_t * table, char *key)
{
  node_t *node = hash_table_get_node(table, key);

  return node != NULL;
}

void
hash_table_remove(hash_table_t * table, char *key)
{
  int index = hash(key) % table->size;

  if (!table->data[index])
    panic("Key is not in the table.");

  node_t *cur = table->data[index];
  node_t *prev = NULL;

  while (cur) {
    if (strcmp(cur->key, key) == 0) {
      if (!prev) {
	table->data[index] = cur->next;
	free(cur);
      } else {
	prev->next = cur->next;
	free(cur->key);
	free(cur);
      }

      return;
    }

    prev = cur;
    cur = cur->next;
  }
}
