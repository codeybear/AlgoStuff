from collections import defaultdict
from heapq import *

def top_k_numbers(arr, k):
  nums = defaultdict(int)
  
  for num in arr:
    nums[num] += 1

  max_heap = []

  for num, freq in nums.items():
    heappush(max_heap, (freq, num))

    if len(max_heap) > k:
      heappop(max_heap)

  output = [item[1] for item in max_heap]
  return output

print(top_k_numbers([1, 3, 5, 12, 11, 12, 11], 2))