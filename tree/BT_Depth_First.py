
class Node:
  def __init__(self, value=0):
    self.value = value
    self.left = None
    self.right = None

    
class Tree:
  def __init__(self):
    self.root = None

  def calc_all_paths(self, target):
    '''Remeber how reference type problems act differently'''
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

  def sum_of_all_paths(self):
    node = self.root
    totals = []
    self.sum_of_all_paths_recurse(node, [], totals)
    return totals

  def sum_of_all_paths_recurse(self, node, nums=None, totals=None):  
    nums.append(node.value)

    if not node.left and not node.right:
      digit = 1
      total = 0

      for num in reversed(nums):
        total += digit * num
        digit *= 10

      totals.append(total)

    if node.left:
      self.sum_of_all_paths_recurse(node.left, nums, totals)

    if node.right:
      self.sum_of_all_paths_recurse(node.right, nums, totals)

    del nums[-1]

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
tree.root = Node(2)
tree.root.left = Node(7)
tree.root.right = Node(1)
tree.root.left.left = Node(9)
tree.root.right.left = Node(3)
tree.root.right.right = Node(5)

print(tree.sum_of_all_paths())