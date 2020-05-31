# python3
from math import floor

class Heap():
    def __init__(self, data):
        self.size = len(data)
        self.heap = data
        self.swaps = []
    def buildHeap(self):
        for i in range(floor((self.size)/2), 0, -1):
            i -= 1
            self._siftdown(i)
        return(self.swaps)
    def _siftdown(self, i):
        min_index = i
        l = self._leftChild(i) 
        if l <= (self.size-1) and self.heap[l] < self.heap[i]:
            min_index = l
        r = self._rightChild(i)
        if r <= (self.size-1) and self.heap[r] < self.heap[min_index]:
            min_index = r
        if i != min_index:
            self._swap(i, min_index)
            self._siftdown(min_index)
    def _leftChild(self, i):
        return(2*i + 1)
    def _rightChild(self, i):
        return(2*i + 2)
    def _swap(self, i, j):
        self.swaps.append((min(i,j),max(i,j)))
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



def build_heap(data):
    heap = Heap(data)
    return heap.buildHeap()


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
