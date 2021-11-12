#include <assert.h>
#include "hash_table.c"
#include "hash_table.h"

#define INIT_SIZE 32

int
main(void)
{
  hash_table_t *table = hash_table_create(INIT_SIZE);

  assert(table != NULL);

  hash_table_add(table, "Milan", 1);
  hash_table_add(table, "Turin", 2);
  hash_table_add(table, "Roma", 3);

  assert(hash_table_get(table, "Turin") == 2);
  assert(hash_table_get(table, "Milan") == 1);

  assert(hash_table_is_in(table, "Roma"));
  assert(!hash_table_is_in(table, "Bologna"));

  hash_table_destroy(table);
  return 0;
}
