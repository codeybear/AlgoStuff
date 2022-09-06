# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        result = num1 + num2
        return self.getList(result)
        
    def getNum(self, l: ListNode) -> int:
        numstr = ""
        
        while True:
            numstr += str(l.val)
            
            if not l.next:
                break
                
            l = l.next
        
        return int(numstr[::-1])

    def getList(self, num) -> ListNode:
        snum = str(num)
        lastNode = ListNode()
        firstNode = lastNode

        for idx, digit in enumerate(snum[::-1]):
            lastNode.val = digit
            
            if idx < len(snum) - 1:   # Need to prevent the creation of an extra node on the end
                lastNode.next = ListNode()
                lastNode = lastNode.next

        return firstNode