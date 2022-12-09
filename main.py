from collections import deque


def topological_sort(vertices, edges):
    '''vertices are nodes, edges are the connections'''
    sortedOrder = []
    
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()

    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract '1' from all of its 
    # a child can't become a source until all parents have been processed
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)

        for child in graph[vertex]:  # get the node's children to decrement their parent links
            inDegree[child] -= 1

        if inDegree[child] == 0:
            sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))

main()