from termios import TABDLY


class Node:
  def __init__(self, value=0):
    self.value = value
    self.left = None
    self.right = None

    
class Tree:
  def __init__(self):
    self.root = None

  def calc_all_paths(self, node, target, paths):
    target = target - node.value
    paths.append[node.value]

    if node.left:
      self.calc_all_paths(node.left, target, paths)

    if node.right:
      self.calc_all_paths(node.right, target, paths)


  def calc_target(self, node, target):
    target = target - node.value
    result = 0

    if target == 0:
      return node.value

    if not node.left and not node.right:
      return 0

    if node.left:
      result = self.calc_target(node.left, target)

    if node.right:
      result += self.calc_target(node.right, target)

    return result

tree = Tree()
tree.root = Node(12)
tree.root.left = Node(7)
tree.root.right = Node(1)
tree.root.left.left = Node(9)
tree.root.right.left = Node(10)
tree.root.right.right = Node(5)

print(tree.calc_all_paths(tree.root, 23, []))