'''
2d matrix problems

All are classed as easy so copied the code from one here

Can navigate the matrix by depth (recursive) or breadth first

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d53be009288Unit

Print out the size of the largest island
'''

def maxAreaIslandDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggestIslandArea = 0

    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == 1):  # only if the cell is a land
                # we have found an island
                biggestIslandArea = max(
                    biggestIslandArea, visitIslandDFS(matrix, i, j))

    return biggestIslandArea


def visitIslandDFS(matrix,  x,  y):
    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
        return 0  # return, if it is not a valid cell
    if (matrix[x][y] == 0):
        return 0  # return, if it is a water cell

    matrix[x][y] = 0  # mark the cell visited by making it a water cell

    area = 1 # counting the current cell
    # recursively visit all neighboring cells (horizontally & vertically)
    area += visitIslandDFS(matrix, x + 1, y)  # lower cell
    area += visitIslandDFS(matrix, x - 1, y)  # upper cell
    area += visitIslandDFS(matrix, x, y + 1)  # right cell
    area += visitIslandDFS(matrix, x, y - 1)  # left cell
    return area

print(maxAreaIslandDFS([
    [1, 1, 1, 0, 0], 
    [0, 1, 0, 0, 1], 
    [0, 0, 1, 1, 0], 
    [0, 1, 1, 0, 0], 
    [0, 0, 1, 0, 0]]))