import math

def triplet_closest_to_target(arr, k):
    arr = sorted(arr)
    min_diff = math.inf
    min_nums = []

    for start_ptr in range(len(arr) - 2):
        mid_ptr = start_ptr + 1
        end_ptr = len(arr) - 1
        target = k - arr[start_ptr]

        while mid_ptr < end_ptr:
            diff = target - arr[mid_ptr] - arr[end_ptr]
            
            if abs(diff) < min_diff:
                min_diff = abs(diff)
                min_nums = [arr[start_ptr], arr[mid_ptr], arr[end_ptr]]

            if diff < 0:
                end_ptr -= 1
            else:
                mid_ptr += 1
            
    return min_nums


print(triplet_closest_to_target([-2, 0, 1, 2, 98, 87, 22], 2))