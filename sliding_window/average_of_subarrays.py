def find_averages_of_subarrays(k, arr):
    start_ptr = 0
    total = 0
    averages = []

    for index, val in enumerate(arr):
        total += val

        if index + 1 - k >= 0:
            averages.append(total / k)
            total -= arr[start_ptr]
            start_ptr += 1

    return averages


result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))

def find_averages_of_subarrays(size, arr):
  '''Second attempt, didn't see a need for a start pointer'''
  output = []
  total = 0

  for index, num in enumerate(arr):
    total += num

    if index - size + 1 >= 0:
      output.append(total / size)
      total -= arr[index - size]
