import heapq

def top_k_numbers(arr, k):
    minheap = arr[:k]
    heapq.heapify(minheap[:k])

    for num in arr[k:]:
        if minheap[0] < num:
            heapq.heappop(minheap)
            heapq.heappush(minheap, num)

    return minheap

print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))

def k_closest_points(arr, k):
    max_heap = []

    for point in range(k):
        heapq.heappush(max_heap, -arr[k])

    # for point in arr:
    #     print(point)

    return 

print(k_closest_points([(1, 2), (3, 4), (2, -1)], 1))