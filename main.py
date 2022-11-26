'''
Dynamic programming coin change problem

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
      return 1

    if amount_new < 0:
      return 0

    combo_count += coin_change(coins, used_new, amount_new)

  return combo_count

# print(coin_change([2, 5, 3, 6], [], 10))
print(coin_change([1, 2, 3], [], 4))