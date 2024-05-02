class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class LinkedList:
  def __init__(self, start_node):
    self._start_node = start_node

  def check_for_loop(self):
    node = self._start_node
    node_fast = self._start_node

    while node:
      print(node.val, node_fast.val)
      node = node.next
      node_fast = node_fast.next
      
      if node_fast: 
        node_fast = node_fast.next
        
        if node_fast is node:
          return True
      else:
        return False
      
    print("No loop found")

node_end = Node(10, None)
node = Node(9, node_end)
node = Node(8, node)
node = Node(7, node)
node = Node(6, node)
node = Node(5, node)
node_end.next = node

list = LinkedList(node)
print(list.check_for_loop())