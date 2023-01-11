from collections import defaultdict


def find_perms(string, perm):
  perms = defaultdict(int)
  start_ptr = 0

  for char in perm:
    perms[char] += 1
  
  for end_ptr, char in enumerate(string):
    if char in perms:
      perms[char] -= 1

      if perms[char] == 0:
        del perms[char]
    else:
      while start_ptr < end_ptr:
        if string[start_ptr] in perm:
          perms[start_ptr] += 1

        start_ptr += 1
    
    if len(perms) == 0:
      return True
      
  return False

print(find_perms("oidbcaf", "abc"))
print(find_perms("odicf", "dc"))
print(find_perms("bcdxabcdy", "bcdyabcdx"))
print(find_perms("aaacb", "abc"))