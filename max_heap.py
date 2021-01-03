import math


class MaxHeap():
    def __init__(self, init=[]):
        self.max_size = 1000
        self.size = len(init)
        self.__h = [None] * self.max_size
        self.__h[:self.size] = init

    def __str__(self):
        return str(self.__h[:self.size])

    def _parent(self, i):
        if i % 2 == 0:
            return i // 2 - 1
        else:
            return i // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, a, b):
        self.__h[a], self.__h[b] = self.__h[b], self.__h[a]

    def _sift_up(self, i):
        while i > 0 and self.__h[self._parent(i)] < self.__h[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _sift_down(self, i):
        max_index = i
        l = self._left_child(i)
        if l <= self.size and self.__h[l] >= self.__h[max_index]:
            max_index = l
        r = self._right_child(i)
        if r <= self.size and self.__h[r] >= self.__h[max_index]:
            max_index = r

        if i != max_index and max_index < self.size:
            self._swap(i, max_index)
            self._sift_down(max_index)

    def insert(self, p):
        if self.size == self.max_size:
            raise Exception("Max size reached")
        self.size += 1

        i = self.size - 1
        self.__h[i] = p
        self._sift_up(i)

    def extract_max(self):
        result = self.__h[0]
        self._swap(0, self.size - 1)
        self.size -= 1
        self._sift_down(0)
        return result

    def remove(self, i):
        self.__h[i] = math.inf
        self._sift_up(i)
        self.extract_max()

    def change_priority(self, i, p):
        old_p = self.__h[i]
        self.__h[i] = p
        if p > old_p:
            self._sift_up(i)
        else:
            self._sift_down(i)


if __name__ == '__main__':
    heap = MaxHeap([42, 29, 18, 14, 7, 18, 12, 11, 13])

    heap.insert(32)
    print(heap)

    print("Max: ", heap.extract_max())
    print(heap)
    print("Max: ", heap.extract_max())
    print(heap)

    heap.remove(2)
    print(heap)

    heap.change_priority(3, 31)
    print(heap)
