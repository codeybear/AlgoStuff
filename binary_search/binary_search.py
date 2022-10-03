'''Binary search that works for ascending order'''

def binary_search(arr, num):
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