from collections import namedtuple


class AssignedJob(namedtuple("AssignedJob", ["worker", "started_at"])):
    def __lt__(self, other):
        return self.started_at < other.started_at

    def __le__(self, other):
        return self.started_at <= other.started_at

    def __gt__(self, other):
        return self.started_at > other.started_at

    def __ge__(self, other):
        return self.started_at >= other.started_at


class MinHeap():
    def __init__(self, init=[]):
        self.__h = init

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
        self.__h[a], self.__h[b] = self.__h[b], self.__h[a]

    def _sift_up(self, i):
        while i > 0 and self.__h[self._parent(i)] > self.__h[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _sift_down(self, i):
        max_index = i
        size = len(self.__h)

        l = self._left_child(i)
        if l < size and self.__h[l] <= self.__h[max_index]:
            max_index = l
        r = self._right_child(i)
        if r < size and self.__h[r] <= self.__h[max_index]:
            max_index = r

        if i != max_index and max_index < size:
            self._swap(i, max_index)
            self._sift_down(max_index)

    def extract_min(self):
        result = self.__h[0]
        self._swap(0, len(self.__h) - 1)
        self.__h.pop()
        self._sift_down(0)
        return result

    def insert(self, p):
        self.__h.append(p)
        self._sift_up(len(self.__h) - 1)


def assign_jobs(n_workers, jobs):
    result = []
    H = MinHeap([AssignedJob(i, 0) for i in range(n_workers)])
    for job in jobs:
        next_worker = H.extract_min()
        result.append(AssignedJob(next_worker.worker, next_worker.started_at))
        H.insert(AssignedJob(next_worker.worker, next_worker.started_at + job))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
