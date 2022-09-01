class Node:
    def __init__(self, Next=None, Value=0) -> None:
        self.next = Next
        self.value = Value

class LinkedList:
    def __init__(self, list = None) -> None:
        node_current = Node()
        self._start_node = node_current

        for index, item in enumerate(list):
            node_current.value = item

            if index == len(list) - 1:
                break

            node_current.next = Node()
            node_current = node_current.next

    def output(self):
        node = self._start_node

        while node:
            print(node.value)
            node = node.next

    def output_recurse(self):
        node = self._start_node
        self.print_node(node)

    def print_node(self, node):
        print(node.value)

        if node.next:
            self.print_node(node.next)

linked = LinkedList([1,2,3,4])
linked.output()
linked.output_recurse()