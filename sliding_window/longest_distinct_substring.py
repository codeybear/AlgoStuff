'''
Given a string, find the length of the longest substring, which has all distinct characters.

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541027921_3Unit

Hard

This is very different to the design gurus code which uses a start and end pointer
'''


def longest_distinct_substring(text):
  longest = 0
  distinct = set()
  
  for char in text:
    if char in distinct:
      length = 0
      distinct = set([char])
    else:
      distinct.add(char)
      longest = max(len(distinct), longest)

  return longest

  
print(longest_distinct_substring("aabccbb"))
print(longest_distinct_substring("abbbb"))
print(longest_distinct_substring("abccdea"))