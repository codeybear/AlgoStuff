'''
Merge k sorted linked lists

In short uses a heap to find the lowest of the k items in the heap
then takes the next item from that list and puts it on the heap

Mostly copied and pasted with some formatting changes

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744411540_108Unit

'''

from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  # used for the min-heap
  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  minHeap = []

  # put the root of each list in the min heap
  for root in lists:
    if root is not None:
      heappush(minHeap, root)

  # take the smallest(top) element from the min-heap and add it to the result
  # if the top element has a next element add it to the heap
  resultHead = None
  resultTail = None

  while minHeap:
    node = heappop(minHeap)

    if resultHead is None:
      resultHead = resultTail = node
    else:
      resultTail.next = node
      # looks weird as we dont create a new node but we are
      # using the node from the heap instead so there is no
      # need
      resultTail = resultTail.next

    if node.next is not None:
      heappush(minHeap, node.next)

  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

