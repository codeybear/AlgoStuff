def solve_knapsack(profits, weights, capacity):
  n = len(profits)
  
  dp = [[0 for x in range(capacity+1)] for y in range(n)]
  
  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  for row in dp: print(row)
      
  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
        
      # exclude the item
      profit2 = dp[i - 1][c]
      
      # take maximum
      dp[i][c] = max(profit1, profit2)

  # maximum profit will be at the bottom-right corner.
  return dp[n - 1][capacity]


def main():
  # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()