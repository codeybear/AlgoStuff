from collections import defaultdict

def max_distinct_substring(text, s):
    max_length = 0
    unique_chars = defaultdict(int)
    start_ptr = 0

    for char in text:
        unique_chars[char] += 1

        while len(unique_chars) > 2:
            start_char = text[start_ptr]

            unique_chars[start_char] -= 1
            
            if unique_chars[start_char] == 0:
                del unique_chars[start_char]

            start_ptr += 1

    print(unique_chars)
    return max_length


print(max_distinct_substring("araaci", s=7))