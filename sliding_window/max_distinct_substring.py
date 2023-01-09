'''https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541009794_1Unit

Longest Substring with K Distinct Characters (medium)

Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.
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
print(max_distinct_substring("cbbebi", 3))