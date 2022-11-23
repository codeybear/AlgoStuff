'''Climbing stairs. Easy dynamic programming example.'''

def climb(length):
  # deal with base cases
  if length == 1:
    return 1

  if length == 2:
    return 2
  
  valid_count = 0
  valid_count += climb(length - 1)
  valid_count += climb(length - 2)

  return valid_count


print(climb(10))


def climbing_stairs(n):
'''How this is often written, from stackoverflow code review'''
  
  if n == 0 or n == 1:
    return 1
  elif n < 0:
    return 0
  else:
    return climbing_stairs(n - 2) + climbing_stairs(n - 1)

print(climbing_stairs(10))