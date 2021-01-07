def go(sum,goal):
  if sum > goal:
    return 0
  elif sum == goal:
    return 1
  else:
    now = 0
    for i in range(1,4):
      now += go(sum+i, goal)
    return now


T = int(input())
for _ in range(T):
  goal = int(input())
  if goal > 11:
    break
  print(go(0,goal))

  
