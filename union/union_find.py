def QuickFindUF():
    def __init__(self, N: int):
        """Initialize the union-find data structure"""
        self.ids = [i for i in range(N)]

    def connected(self, p, q: int) -> bool:
        """check if p and q are connected
        """
        return self.ids[p] == self.ids[q]

    def union(self, p, q: int):
        """add the connection between p and q
        """
        pid = self.ids[p]
        qid = self.ids[q]

        # change all entries with ids[p] to ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid


def QuickUnionUF():
    def __init__(self, N: int):
        """Initialize the union-find data structure"""
        self.ids = [i for i in range(N)]

    def root(self, i: int):
        while i != self.ids[i]:
            i = self.ids[i]
        return i

    def connected(self, p, q: int) -> bool:
        """check if p and q are connected
        """
        return self.root(p) == self.root(q)

    def union(self, p, q: int):
        """add the connection between p and q
        """
        rp = self.root(p)
        rq = self.root(q)
        self.ids[rp] = rq


def WeightedQuickUnionUF():
    def __init__(self, N: int):
        """Initialize the union-find data structure"""
        self.ids = [i for i in range(N)]
        # count the number of nodes in each root
        # (union-by-size)
        self.sizes = [1 for i in range(N)]

    def root(self, i: int):
        while i != self.ids[i]:
            # update root gradually
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def connected(self, p, q: int) -> bool:
        """check if p and q are connected
        """
        return self.root(p) == self.root(q)

    def union(self, p, q: int):
        """add the connection between p and q
        """
        rp = self.root(p)
        rq = self.root(q)
        if rp == rq:
            return

        # link root of smaller tree to larger tree
        if self.sizes[rp] < self.sizes[rq]:
            self.ids[rp] = rq
            self.ids[rq] += self.sizes[rp]
        else:
            self.ids[rq] = rp
            self.ids[rp] += self.sizes[rq]
