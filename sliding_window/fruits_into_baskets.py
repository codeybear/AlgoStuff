'''
Fruits into baskets

Medium

Sliding window problem very similar to max_distinct_substring.py

https://designgurus.org/path-player?courseid=grokking-the-coding
-interview&unit=grokking-the-coding-interview_1628541018393_2Unit
'''

def fruits(arr):
  counter = {}
  start_ptr = 0
  max_count = 0

  for end_ptr, fruit in enumerate(arr):
    if fruit in counter:
      counter[fruit] += 1
    else:
      counter[fruit] = 1

    while len(counter) > 2:
      start_fruit = arr[start_ptr]
      counter[start_fruit] -= 1

      if counter[start_fruit] == 0:
        del counter[start_fruit]

      start_ptr += 1

    max_count = max(max_count, end_ptr - start_ptr + 1)

  return max_count


print(fruits(['A', 'B', 'C', 'A', 'C']))
print(fruits(['A', 'B', 'C', 'B', 'B', 'C']))
