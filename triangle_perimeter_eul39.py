# euler 39 - https://projecteuler.net/problem=39
# Uses the relation a^2 = b^2 + c^2
# This means that the result of a^2 + b^2 must be square rootable to an integer
# So I am caching all the numbers from 1 to 1000 to be able to check this quickly
# This method also removes the need to calculate the square root which is slower

from collections import defaultdict

squares = {}
side_length_count = defaultdict(int)

for i in range(1000):
  squares[i**2] = i

for a in range(1, 1000):
  for b in range(a, 1000):
    c2 = a**2 + b**2
    
    if (c2) in squares:
      c = squares[c2]
      if(a+b+c) > 1000: break
      side_length_count[a+b+c] += 1

# print out which side perimeter is the highest
num = max(side_length_count, key=side_length_count.get)
value = side_length_count[num]
print(num, value)