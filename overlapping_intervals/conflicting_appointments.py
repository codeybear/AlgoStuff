'''
Merge intervals 
Conflicting appointments problem (medium)
Brute force O(N^2) and O(N) version included

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743642980_24Unit
'''

def find_overlapping_appointments_brute(apps):
  apps.sort(key=lambda x: x[0])

  for current_idx, current_app in enumerate(apps):
    for next_idx in range(current_idx + 1, len(apps)):
      if current_app[1] > apps[next_idx][0]:
        print(current_app, apps[next_idx])
  
  return apps


def find_overlapping_appointments(apps):
  apps.sort(key=lambda x: x[0])
  max_end = 0
  overlaps = set()

  for index in range(len(apps) - 1):
    max_end = max(max_end, apps[index][1])

    if max_end > apps[index + 1][0]:
      overlaps.append(apps[index])
      overlaps.append(apps[index + 1])

  return overlaps
  
# test data 2,6 overlaps the next two, 3,4 doesn't overlap with the next one
print(find_overlapping_appointments([[2,6], [3,4], [5,6], [7,8], [7,10]]))