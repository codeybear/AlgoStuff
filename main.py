def find_averages_of_subarrays(k, arr):
    start_ptr = 0
    total = 0
    averages = []

    for index, val in enumerate(arr):
        total += val

        if index + 1 - k >= 0:
            averages.append(total / (index - start_ptr + 1))
            total -= arr[start_ptr]
            start_ptr += 1

    return averages


result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))
