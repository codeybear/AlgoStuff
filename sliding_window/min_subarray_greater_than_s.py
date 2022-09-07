import math


def min_subarray_greater_than_s(arr, s):
    min_length = math.inf
    start_index = 0
    total = 0

    for end_index, num in enumerate(arr):
        total += num

        while total >= s:
            min_length = min(min_length, end_index - start_index + 1)
            total -= arr[start_index]
            start_index += 1    # note start index could become higher than end_index, but only by one

        print(start_index, end_index)
    if min_length == math.inf: return 0

    return min_length


print(min_subarray_greater_than_s([2, 10, 5, 2, 3, 2], s=7))