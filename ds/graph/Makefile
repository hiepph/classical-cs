all:
	gcc -g -o bin/test test.c graph.c \
		../queue/queue.c ../priority_queue/priority_queue.c \
		-I../queue -I../priority_queue

test:
	bin/test

clean:
	rm -rf bin/*
