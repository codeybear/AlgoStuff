
from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def level_order_traversal_simple(self):
        '''Pushing the child nodes to a queue (appendleft) and popping from the right
        is enough to ensure the it is traversed in order with any special "level"
        variables'''
        output = []
        current = deque([self.root])

        while current:
            next = deque()   # keep a track of the child nodes from the current iteration 
            node = current.pop()
            output.append(node.value)

            if node.left:
                current.appendleft(node.left)

            if node.right:
                current.appendleft(node.right)
    
        return output      

  
    def level_order_averages(self):
      '''Doing something like an average requires tracking the current number of nodes
      on the current level'''
      output = []
      current = deque([self.root])

      # trying the method described by design gurus using a queue rather than a list
      while current:
        length = len(current)
        average = 0

        for idx in range(length):
          node = current.pop()
          average += node.value

          if node.left:
            current.appendleft(node.left)

          if node.right:
            current.appendleft(node.right)

        output.append(average / length)
            
      return output
      
        
tree = BinaryTree(10)
tree.root.left = Node(7)
tree.root.right = Node(21)
tree.root.left.left = Node(9)
tree.root.right.left = Node(10)
tree.root.right.right = Node(5)
# print(tree.level_order_traversal())
print(tree.level_order_averages())