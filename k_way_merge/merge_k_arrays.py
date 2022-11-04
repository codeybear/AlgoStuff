'''
Merge k lists using merge style combining

Medium

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744417564_109Unit
'''

from heapq import *


def merge_k_arrays(lists):
  heap = []

  for list in lists:
    heappush(heap, (list[0], 0, list))

  output = []

  while len(heap) > 0:
    lowest, index, list = heappop(heap)
    output.append(lowest)
    
    index += 1

    if index != len(list):
      heappush(heap, (list[index], index, list))

  return output


print(merge_k_arrays([[2, 6, 8], [3, 6, 7], [1, 3, 4]]))