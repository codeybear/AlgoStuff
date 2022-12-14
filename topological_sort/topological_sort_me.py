from collections import deque
from collections import defaultdict


def topo_sort(_, edges):
  adjacent = defaultdict(list)
  in_degrees = defaultdict(int)

  for parent, child in edges:
    in_degrees[child] += 1    
    adjacent[parent].append(child)

  sources = deque()
  
  # find the nodes with no parents
  for parent, _ in adjacent.items():
    if parent not in in_degrees:
      sources.append(parent)

  output = []

  while sources:
    source = sources.popleft()
    output.append(source)
    
    for child in adjacent[source]:
      in_degrees[child] -=1

      if in_degrees[child] == 0:
        sources.append(child)
      
  return output


print(topo_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
print(topo_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))