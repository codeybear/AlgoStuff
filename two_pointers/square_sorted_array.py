''' Squaring a Sorted Array (easy) 

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Array contains negative numbers

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743435284_3Unit
'''


def square_sorted_array(arr):
    arr_sorted = []
    start_ptr = 0
    end_ptr = 0

    # find the index of zero
    for idx, num in enumerate(arr):
        if num >= 0:
            end_ptr = idx
            start_ptr = idx - 1
            break

    # end pointer moves forwards, start pointer moved backwards
    # add the square of the smaller of the two amounts first
    while len(arr_sorted) < len(arr):
        print(start_ptr, end_ptr, arr_sorted)
        neg = arr[start_ptr]
        pos = arr[end_ptr]

        if abs(neg) > pos:
            arr_sorted.append(pos**2)

            if end_ptr != 0:
                end_ptr += 1
        else:
            arr_sorted.append(neg**2)

            if start_ptr != len(arr) - 1:
                start_ptr -= 1

    return arr_sorted

print(square_sorted_array([-2, -1, 0, 2, 3]))
