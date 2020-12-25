from collections import deque

def max_sliding_window_naive(sequence, m):
    q = deque()
    ans = []
    for i, num in enumerate(sequence):
        # keep only in sliding window
        if q and q[0] <= i - m:
            q.popleft()

        # keep a decreasing sliding window
        while q and num >= sequence[q[-1]]:
            q.pop()
        q.append(i)

        # get 0-th index for each step
        ans.append(sequence[q[0]])

    # skip initial values
    return ans[m-1:]

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
