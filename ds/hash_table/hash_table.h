typedef struct hash_table hash_table_t;
typedef struct node node_t;

/*
 * Create a new hash table with defined size
 */
hash_table_t *hash_table_create(const int size);


void hash_table_destroy(hash_table_t * table);
