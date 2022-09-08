from collections import defaultdict

def max_distinct_substring(text, k):
    max_length = 0
    length = 0
    unique_chars = defaultdict(int)
    start_ptr = 0

    for char in text:
        unique_chars[char] += 1
        length += 1

        while len(unique_chars) > k:
            start_char = text[start_ptr]

            unique_chars[start_char] -= 1
            
            if unique_chars[start_char] == 0:
                del unique_chars[start_char]

            start_ptr += 1
            length -= 1

        max_length = max(max_length, length)
      
    return max_length


print(max_distinct_substring("cbbebi", k=3))