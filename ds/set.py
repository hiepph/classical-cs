class Set():
    def __init__(self, n):
        self.parent = [None] * n
        self.rank = [0] * n

    def __str__(self):
        return f"parent: {self.parent}\nrank:   {self.rank}"

    def make(self, i):
        self.parent[i] = i

    def find(self, i):
        # while i != self.parent[i]:
        #     i = self.parent[i]
        # return i
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


if __name__ == '__main__':
    s = Set(7)
    for i in range(1, 7):
        s.make(i)
    s.union(2, 4)
    s.union(5, 4)
    s.union(3, 1)
    s.union(2, 3)
    s.union(2, 6)
    print(s)
