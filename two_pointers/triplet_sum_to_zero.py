'''Triplet Sum to Zero (medium)

First attempt was pretty easy however need to skip duplicate elements
so checks such as: 
if arr[start_ptr] == arr[start_ptr - 1]: continue
'''


def triplet_sum_to_zero(arr):
    start_ptr, mid_ptr, end_ptr = 0,0,0
    arr = sorted(arr)

    for start_ptr in range(len(arr)-2):
        mid_ptr = start_ptr + 1
        end_ptr = len(arr) - 1
        target = 0 - arr[start_ptr]

        while mid_ptr < end_ptr:
            mid_num = arr[mid_ptr]
            end_num = arr[end_ptr]

            if mid_num + end_num == target:
                print(arr[start_ptr], arr[mid_ptr], arr[end_ptr])
                mid_ptr += 1
                end_ptr -= 1
            elif mid_num + end_num > target:
                end_ptr -= 1
            else:
                mid_ptr += 1

    return arr

print(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
print(triplet_sum_to_zero([-5, 2, -1, -2, 3]))