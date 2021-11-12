#include <assert.h>
#include "hash_table.c"
#include "hash_table.h"

#define INIT_SIZE 128

int
main(void)
{
  hash_table_t *table = hash_table_create(INIT_SIZE);

  assert(table != NULL);

  hash_table_destroy(table);
  return 0;
}
