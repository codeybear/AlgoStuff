def binary_search(arr, num):
    '''Binary search that works for ascending order'''
    start = 0
    end = len(arr) - 1

    while True:
        mid = start + (end - start) // 2

        if arr[mid] == num:
            return mid
        
        if num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))


def binary_search_ceiling(arr, num):
    '''Binary search for the smallest number greater than or equal to'''
    start = 0
    end = len(arr) - 1
    smallest = float('inf')

    if arr[len(arr) - 1] < num:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == num:
            return mid
        
        if num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
            smallest = min(smallest, arr[mid])

    return smallest

print(binary_search_ceiling([1, 3, 8, 10, 15], 12))
print(binary_search_ceiling([4, 6, 10], 17))