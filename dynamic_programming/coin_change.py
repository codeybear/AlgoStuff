'''
Dynamic programming coin change problem

https://www.geeksforgeeks.org/coin-change-dp-7
'''

def coin_change(coins, used, amount):
    '''
    First attempt that needs to check for duplicates.
    '''
    combo_count = 0
    
    for coin in coins:
        used_new = used[:]
        used_new.append(coin)

        amount_new = amount - coin

        if amount_new == 0: 
            print(used_new)
            # we need to pass up the result of previous iterations
            return combo_count + 1

        if amount_new < 0:
            return combo_count

        combo_count += coin_change(coins, used_new, amount_new)

    return combo_count

# print(coin_change([2, 5, 3, 6], [], 10))
# print(coin_change([1, 2, 3], [], 4))


def coin_change_correct(coins, n, sum): 
    '''
    Coin change dp solution.

    Copied from geeks4geeks and tidied up

    Uses the include/exclude method which is also given by the knapsack solution

    This method descends through number of items - including and excluding each item
    This means you will get 4p = 2,1,1 but not 1,2,1 or 1,1,2 i.e. combinations no permutations
    '''
    # If sum is 0 then there is 1 solution (do not include any coin)
    if (sum == 0):
        return 1
 
    # If sum is less than 0 then no solution exists
    if (sum < 0):
        return 0
 
    # If there are no coins and sum is greater than 0, then no solution exist
    if (n <= 0):
        return 0
 
    # count is sum of solutions (i)
    return coin_change_correct(coins, n - 1, sum) + coin_change_correct(coins, n, sum-coins[n-1])

 
# Driver program to test above function
coins = [1, 2, 3]
n = len(coins)
print(coin_change_correct(coins, n, 4))