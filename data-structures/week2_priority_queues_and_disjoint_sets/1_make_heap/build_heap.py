class MinHeap():
    def __init__(self, init=[]):
        self.size = len(init)
        self.__h = init
        self.swaps = []

    def __str__(self):
        return str(self.__h)

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
        self.swaps.append((a, b))
        self.__h[a], self.__h[b] = self.__h[b], self.__h[a]

    # def _sift_up(self, i):
    #     while i > 0 and self.__h[self._parent(i)] < self.__h[i]:
    #         self._swap(i, self._parent(i))
    #         i = self._parent(i)

    def _sift_down(self, i):
        max_index = i
        l = self._left_child(i)
        if l < self.size and self.__h[l] <= self.__h[max_index]:
            max_index = l
        r = self._right_child(i)
        if r < self.size and self.__h[r] <= self.__h[max_index]:
            max_index = r

        if i != max_index and max_index < self.size:
            self._swap(i, max_index)
            self._sift_down(max_index)

    def build(self):
        for i in range(self.size // 2, -1, -1):
            self._sift_down(i)

def build_heap(data):
    """Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    H = MinHeap(data)
    H.build()

    return H.swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
