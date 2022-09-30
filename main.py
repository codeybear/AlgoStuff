def combos(nums):
  combos = []
  combos.append([])
  
  for num in nums:
    for combo in combos:
      new_combo = list(combo)
      new_combo.append(num)
      combos.append(new_combo)
    
print(combos([1, 5, 3]))