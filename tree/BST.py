class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root:Node = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root

        while True:
            if value == node.value:
                return
            elif value > node.value:
                if not node.right:
                    node.right = Node(value)
                    return

                node = node.right
            else:
                if not node.left:
                    node.left = Node(value)
                    return

                node = node.left


    def print_inorder(self, node = None):
        """This is a depth first traversal (left, root, right)."""
        if not node:
            node = self.root

        if node.left:
            self.print_inorder(node.left)

        print(node.value)

        if node.right   :
            self.print_inorder(node.right)

    def print_by_level(self):
        """Level order traveral of a binary tree problem.

        This is effectively a breadth first traversal
        www.codinginterview.com/amazon-interview-questions
        """
        nodes = [self.root]
        output = []

        while nodes:
            next_level = []  # maybe not efficient clearing a list, could append pop from the queueS

            for node in nodes:
                output.append(node.value)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            nodes = next_level
            
        return output


bst = BST()
bst.add(30)
bst.add(50)
bst.add(15)
bst.add(20)
bst.add(10)
bst.add(40)
bst.add(60)
bst.print_inorder()
print(bst.print_by_level())
