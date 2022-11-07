'''
All based on properties of xor

Problems have other solutions but can use more memory or could cause an overflow (adding all the number together)

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744227261_87Unit
'''

def find_missing_number(arr):
  '''Solution without xor. Time is o(n) but we could get an integer overflow'''
  n = len(arr) + 1
  # find sum of all numbers from 1 to n.
  s1 = 0
  for i in range (1, n+1):
    s1 += i

  # subtract all numbers in input from sum.
  for i in arr:
    s1 -= i
  
  # s1, now, is the missing number
  return s1

arr = [1, 5, 2, 6, 4] 
print(f'Missing number is: {find_missing_number(arr)}')

def find_missing_number(arr):
  '''Same as above using xor, no chance of integer overflow'''
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1

  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]

  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2

def find_single_number(arr):
    '''Works because x ^ x = 0 so duplicates are removed'''
    num = 0
    for i in arr:
        num ^= i
    return num

arr = [1, 4, 2, 1, 3, 2, 3]
print(f"Find single number is: {find_single_number(arr)}")