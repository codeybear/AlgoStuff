'''
Find all permutations (medium)

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744061506_69Unit

"When we add a new number, we take each permutation of the previous step and insert the new number in every position to generate the new permutations". These new permutations replace the old ones
'''

def find_permutations(nums):
  perms = []
  perms.append([])

  for num in nums:    
    new_perms = []  # holds the new permutations created from the previous iteration
                    # this will replace the old items with the new digit inserted
    for perm_idx in range(len(perms)):

      # For the current permutation insert the new digit
      for pos in range(len(perms[perm_idx]) + 1):
        perm = list(perms[perm_idx])   # careful to take a copy 
        perm.insert(pos, num)
        new_perms.append(perm)

    perms = new_perms # the old perms are replaced
        
  return perms

print(find_permutations([1, 3, 5]))