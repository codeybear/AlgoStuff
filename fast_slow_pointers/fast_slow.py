'''
LinkedList Cycle (easy)

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743546476_13Unit
'''

class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.node = None

    def add(self, value):
        if not self.node:
            self.node = Node(value)

        node = self.node

        while node.next:
            node = node.next

        node.next = Node(value)

    def print(self):
        node = self.node

        while node:
            print(node.value)
            node = node.next

    def load_circle(self):
        loop_node = Node(1)
        self.node = loop_node
        self.node.next = Node(12)
        self.node.next.next = Node(14)
        self.node.next.next.next = Node(16)
        self.node.next.next.next.next = loop_node

    def check_cycle(self):
        slow_node = self.node
        fast_node = self.node

        # notice we can go two steps at time for the fast and worry about the number of items
        # if there is no cycle in the linked list then it won't matter
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            print(fast_node, slow_node)

            if fast_node == slow_node:
                return True

        return False


linked = LinkedList()
linked.load_circle()
linked.print()
print(linked.check_cycle())