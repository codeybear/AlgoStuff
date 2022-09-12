'''Don't know where this came from, relatively easy'''

import math

def find_closest_sum_in_list(arr, target):
    start_ptr = 0
    end_ptr = len(arr) - 1
    min_total = math.inf

    while start_ptr != end_ptr:
        total = target - (arr[start_ptr] + arr[end_ptr])

        if total >= 0:
            min_total = min(total, min_total)

        if total > 0:
            start_ptr += 1
        else:
            end_ptr -= 1

    return min_total


print(find_closest_sum_in_list([10, 22, 28, 29, 30, 40], 54))
print(find_closest_sum_in_list([1, 3, 4, 7, 10], 15))
