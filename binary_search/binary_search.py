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


def binary_search_char_ceiling(arr, char):
    '''find the smallest character greater than a character in a circular array'''
    start = 0
    end = len(arr) - 1
    smallest = 'z'

    # array is circular so the start element is greater than the end one
    if char >= arr[len(arr) - 1]:
        return arr[0]

    while start <= end:
        mid = end - (end - start) // 2
        current = arr[mid]

        if char < current:
            end = mid - 1
            smallest = min(smallest, current)
        else:
            start = mid + 1

    return smallest

print(binary_search_char_ceiling(['a', 'c', 'f', 'h'], 'd'))
print(binary_search_char_ceiling(['a', 'c', 'f', 'h'], 'b'))
print(binary_search_char_ceiling(['a', 'c', 'f', 'h'], 'm'))
print(binary_search_char_ceiling(['a', 'c', 'f', 'h'], 'c'))
print(binary_search_char_ceiling(['a', 'c', 'f', 'h'], 'h'))