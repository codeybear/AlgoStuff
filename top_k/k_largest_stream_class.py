from heapq import *

class k_largest:
    def __init__(self, arr, k):
        self.k = k
        self.heap = []
        
        for num in arr:
            self.add(num)

    def add(self, num):
        heappush(self.heap, num)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]


largest = k_largest([3, 1, 5, 12, 2, 11], 4)
print(largest.add(6))
print(largest.add(13))
print(largest.add(4))
