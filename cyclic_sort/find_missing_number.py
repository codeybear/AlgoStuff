''' 
Cyclic sort - missing number 
This is zero based and there is a number that is one too high for the array
skipping this item means that it always falls into the place of the
missing item
'''

def find_missing_number(arr):
  idx = 0
  
  while idx < len(arr):
    num = arr[idx]

    if num != idx and num != len(arr):
      temp = arr[num]
      arr[num] = num
      arr[idx] = temp
    else:
      idx += 1 

  print(arr)
  
  for idx, num in enumerate(arr):
    if idx != num:
      return idx

print(cyclic_sort([4, 0, 3, 1]))
print(cyclic_sort([8, 3, 5, 2, 4, 6, 0, 1]))