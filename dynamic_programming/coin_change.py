'''
Dynamic programming coin change problem

First attempt that needs to check for duplicates.

https://www.geeksforgeeks.org/coin-change-dp-7
'''

def coin_change(coins, used, amount):
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

print(coin_change([2, 5, 3, 6], [], 10))
# print(coin_change([1, 2, 3], [], 4))