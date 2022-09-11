'''Longest Substring with K Distinct Characters (medium)

One of the tests where a dict is needed to track character frequency

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541009794_1Unit
'''

from collections import defaultdict

def max_distinct_substring(text, k):
    max_length = 0
    unique_chars = defaultdict(int)
    start_ptr = 0

    for end_ptr, char in enumerate(text):
        unique_chars[char] += 1

        while len(unique_chars) > k:
            start_char = text[start_ptr]
            unique_chars[start_char] -= 1
            
            if unique_chars[start_char] == 0:
                del unique_chars[start_char]

            start_ptr += 1

        max_length = max(max_length, end_ptr - start_ptr + 1)

    return max_length


print(max_distinct_substring("araaci", 2))