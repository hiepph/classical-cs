CC=gcc
CFLAGS=-g -Wall -pedantic


all: test_binary_search_recursive test_binary_search_iterative

test: all
	./test_binary_search_recursive
	./test_binary_search_iterative

test_binary_search_recursive: test.o binary_search_recursive.o
	$(CC) $(CFLAGS) -o $@ $^

test_binary_search_iterative: test.o binary_search_iterative.o
	$(CC) $(CFLAGS) -o $@ $^

test.o: test.c binary_search.h

binary_search_recursive.o: binary_search_recursive.c  binary_search.h
binary_search_iterative.o: binary_search_iterative.c  binary_search.h

clean:
	$(RM) ./test_binary_search_recursive ./test_binary_search_iterative *.o
