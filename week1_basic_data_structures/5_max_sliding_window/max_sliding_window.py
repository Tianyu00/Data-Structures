# reference: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

# python3


def max_sliding_window_naive(sequence, m):
    q = []
    for i in range(m):
        while q and sequence[i]>=sequence[q[-1]]:
            q.pop()
        q.append(i)
    maximums = [sequence[q[0]]]
    for i in range(m,len(sequence)):
        if q[0] < i-m+1:
            q.pop(0)
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
        maximums.append(sequence[q[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

