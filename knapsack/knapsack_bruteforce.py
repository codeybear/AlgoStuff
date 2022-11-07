def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    '''Splits into two directions at each level, both processing 
    (subtracting the weight an capacity) and skipping the current item'''
    # base checks
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # this can look weired but we are doing depth first and passing this point on
    # all calls in the stack first before calculating
    profit1 = 0

    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_recursive(
        profits, weights, capacity - weights[current_index], current_index + 1)

    # notice no deductions to weights and capacities as we are skipping the current item
    profit2 = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()