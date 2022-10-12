import heapq
import math

def top_k_numbers(arr, k):
    minheap = arr[:k]
    heapq.heapify(minheap[:k])

    for num in arr[k:]:
        if minheap[0] < num:
            heapq.heappop(minheap)
            heapq.heappush(minheap, num)

    return minheap

# print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))

def k_closest_points(arr, k):
    max_heap = []

    for point in range(k):
        size = distance(arr[point][0], arr[point][1])
        heapq.heappush(max_heap, -size)

    print(max_heap)
  
    for point in range(k, len(arr)):
        size = distance(arr[point][0], arr[point][1])
        print(size)
        if -max_heap[0] > size:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -size)

    return max_heap

# print(k_closest_points([(1, 3), (3, 4), (2, -1)], 2))

def distance(x, y):
  return math.sqrt(x**2 + y**2)
  
