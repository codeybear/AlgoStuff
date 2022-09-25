from tree.BT import *

tree = BinaryTree(10)
tree.root.left = Node(7)
tree.root.right = Node(21)
tree.root.left.left = Node(9)
tree.root.right.left = Node(10)
tree.root.right.right = Node(5)
# print(tree.level_order_traversal())
print(tree.level_order_averages())