def find_sum_in_list(arr, target):
    start_ptr = 0
    end_ptr = len(arr) - 1

    while start_ptr != end_ptr:
        sum = arr[start_ptr] + arr[end_ptr]

        if sum == target:
            return (start_ptr, end_ptr)
        elif sum > target:
            end_ptr -= 1
        else:
            start_ptr +=1

print(find_sum_in_list([2,4,6,9,11,15], 10))