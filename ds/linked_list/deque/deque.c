#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <assert.h>

#include "deque.h"

#define NUM_DIRECTIONS 2

struct deque {
    struct deque *next[NUM_DIRECTIONS];
    int value;
};

// return a new empty deque
Deque* deque_new(void)
{
    Deque *d;

    // don't use value in dummy head
    d = malloc(offsetof(struct deque, value));

    if (d) {
        d->next[DEQUE_FRONT] = d->next[DEQUE_BACK] = d;
    }

    return d;
}

int deque_empty(const Deque* d)
{
    return d->next[DEQUE_FRONT] == d;
}

void deque_push(Deque* d, int direction, int value)
{
    struct deque *l;

    assert(direction == DEQUE_FRONT || direction == DEQUE_BACK);

    // new element
    l = malloc(sizeof(struct deque));
    assert(l);
    l->value = value;

    // insert the new element inside the chain
    l->next[direction] = d->next[direction];
    l->next[!direction] = d;
    l->next[direction]->next[!direction] = l;
    d->next[direction] = l;
}


void deque_destroy(Deque *d)
{
    while(!deque_empty(d)) {
        deque_pop(d, DEQUE_FRONT);
    }
    free(d);
}

int deque_pop(Deque* d, int direction)
{
    struct deque *l;
    int v;

    assert(direction == DEQUE_FRONT || direction == DEQUE_BACK);
    l = d->next[direction];
    if (l == d) {
        return DEQUE_EMPTY;
    }

    // repoint the chain
    d->next[direction] = l->next[direction];
    d->next[direction]->next[!direction] = d;

    v = l->value;
    free(l);
    return v;
}

int main(int argc, char **argv)
{
    int i;
    int n;
    Deque *d;

    if(argc != 2) {
        fprintf(stderr, "Usage: %s iterations\n", argv[0]);
        return 1;
    }
    n = atoi(argv[1]);

    d = deque_new();
    assert(deque_empty(d));

    for(i = 0; i < n; i++) {
        deque_push(d, DEQUE_FRONT, i);
        assert(!deque_empty(d));
    }

    for(i = 0; i < n; i++) {
        assert(deque_pop(d, DEQUE_BACK) == i);
    }

    assert(deque_empty(d));

    for(i = 0; i < n; i++) {
        deque_push(d, DEQUE_BACK, i);
        assert(!deque_empty(d));
    }

    for(i = 0; i < n; i++) {
        assert(deque_pop(d, DEQUE_FRONT) == i);
    }

    assert(deque_empty(d));

    for(i = 0; i < n; i++) {
        deque_push(d, DEQUE_BACK, i);
        assert(!deque_empty(d));
    }

    for(i = n-1; i >= 0; i--) {
        assert(deque_pop(d, DEQUE_BACK) == i);
    }

    assert(deque_empty(d));

    for(i = 0; i < n; i++) {
        deque_push(d, DEQUE_FRONT, i);
    }

    for(i = n-1; i >= 0; i--) {
        assert(deque_pop(d, DEQUE_FRONT) == i);
    }

    assert(deque_empty(d));

    assert(deque_pop(d, DEQUE_FRONT) == DEQUE_EMPTY);

    assert(deque_pop(d, DEQUE_BACK) == DEQUE_EMPTY);

    deque_push(d, DEQUE_FRONT, 12);

    deque_destroy(d);

    return 0;
}
