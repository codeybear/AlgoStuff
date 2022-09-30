'''
https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744042826_67Unit

"We can start with an empty set, iterate through all numbers one-by-one, and add them to existing sets to create new subsets."

Described as a breadth first method

Easy problem
'''

def combos(nums):
  combos = []
  # create a blank subset so when we take a copy there will be a number on its own
  combos.append([])
  
  for num in nums:
    for i in range(len(combos)):
      combo = combos[i]
      new_combo = list(combo)
      new_combo.append(num)
      combos.append(new_combo)
      
  return combos
    
print(combos([1, 5, 3]))