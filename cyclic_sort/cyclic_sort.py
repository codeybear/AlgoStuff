''' Cyclic sort - number indicate positions '''

def cyclic_sort(arr):
  idx = 0
  
  while idx < len(arr):
    num = arr[idx]

    if num - 1 != idx:
      temp = arr[num - 1]
      arr[num - 1] = num
      arr[idx] = temp
    else:
      # important to only progress when the current number is in the correct position
      idx += 1 

  return arr

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))