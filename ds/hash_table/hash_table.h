typedef struct hash_table hash_table_t;
typedef struct node node_t;

/*
 * Create a new hash table with defined size
 */
hash_table_t *hash_table_create(const int size);

void hash_table_destroy(hash_table_t * table);


/*
 * Hash function
 * key: string needed to be hashed
 * size: size of the table.
 */
int hash(char *key);

/*
 * Get the value based on key
 */
int hash_table_get(hash_table_t * table, char *key);

/*
 * Add new key-value to the table.
 * If key exists, update the value.
 */
void hash_table_add(hash_table_t * table, char *key, int value);
