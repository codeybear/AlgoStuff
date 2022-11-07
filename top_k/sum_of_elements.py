'''
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Medium problem

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744351402_102Unit
'''

from heapq import *

def sum_of_elements(arr, k1, k2):
  heap = []
  
  for num in arr:
    heappush(heap, num)

  total = 0
  size_count = 1
  
  for _ in range(len(heap)):
    num = heappop(arr)
    
    if k1 < size_count < k2:
      total += num

    if size_count >= k2:
      break

    size_count += 1

  return total


print(sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))