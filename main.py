
class Node:
  def __init__(self, value=0):
    self.value = value
    self.left = None
    self.right = None

    
class Tree:
  def __init__(self):
    self.root = None

  def calc_all_paths(self, target):
    all_paths = []
    self.calc_all_paths_recurse(self.root, target, [], all_paths)
    return all_paths

  def calc_all_paths_recurse(self, node, target, paths, all_paths):
    target = target - node.value
    paths.append(node.value)
    
    if target == 0:
      all_paths.extend(paths)
      
    if node.left:
      self.calc_all_paths_recurse(node.left, target, paths, all_paths)

    if node.right:
      self.calc_all_paths_recurse(node.right, target, paths, all_paths)

    del paths[-1]

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

print(tree.calc_all_paths(23))