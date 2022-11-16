'''Climbing stairs. Easy dynamic programming example'''

def climb(length):
  # deal with base cases
  if length == 0:
    return 1

  if length < 0:
    return 0
  
  valid_count = 0
  valid_count += climb(length - 1)
  # print(climb(length - 1), length - 1)
  valid_count += climb(length - 2)
  # print(climb(length - 2), length - 2)

  return valid_count


print(climb(10))