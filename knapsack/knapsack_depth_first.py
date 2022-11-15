'''
knapsack depth first approach

Not very clear from the website but explained a little better here

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744460476_114Unit

'''

def knapsack_depth_first(profits, weights, capacity):
    n = len(profits)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]

    # initialise the first row, we always take this item
    for c in range(0, capacity+1):
        if weights[0] <= c:
          dp[0][c] = profits[0]

    for row in dp: print(row)

    # process all sub-arrays after the first for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0,0

            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]

            # exclude the item
            profit2 = dp[i - 1][c]

            # take maximum
            dp[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


print(knapsack_depth_first([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(knapsack_depth_first([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(knapsack_depth_first([1, 6, 10, 16], [1, 2, 3, 5], 7))
