# brute force version, need better test data

def find_overlapping_appointments(apps):
  apps.sort(key=lambda x: x[0])

  for current_idx, current_app in enumerate(apps):
    for next_idx in range(current_idx + 1, len(apps)):
      if current_app[1] > apps[next_idx][0]:
        print(current_app, apps[next_idx])
  
  # return apps

print(find_overlapping_appointments([(2, 5), (7, 9), (1, 4)]))