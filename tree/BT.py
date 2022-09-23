
from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def level_order_traversal(self):
        output = []
        current = deque()
        next = deque()
        current.append(self.root)

        while next:
            next = deque()

            while current:
                node = current.pop()
                output.append(node.value)

                if node.left:
                    next.append(node.left)

                if node.right:
                    next.append(node.right)
            
            current = next

        return output

        

tree = BinaryTree(10)
tree.root.left = Node(7)
tree.root.right = Node(21)
tree.root.left.left = Node(9)
tree.root.right.left = Node(10)
tree.root.right.right = Node(5)
print(tree.level_order_traversal())
