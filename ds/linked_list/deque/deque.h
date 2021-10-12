// ref: https://cs.yale.edu/homes/aspnes/classes/223/notes.html#Looping_over_a_linked_list

typedef struct deque Deque;

#define DEQUE_FRONT (0)
#define DEQUE_BACK (1)

#define DEQUE_EMPTY (-1)

// return a new empty deque
Deque* deque_new(void);

// push new value
void deque_push(Deque* d, int direction, int value);

// pop first value
// return DEQUE_EMPTY if deque is empty
int deque_pop(Deque* d, int direction);

// return 1 if deque contains no elements, 0 otherwise
int deque_empty(const Deque* d);

// free space occupied by deque
void deque_destroy(Deque *d);
