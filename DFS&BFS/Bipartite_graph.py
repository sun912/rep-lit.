k = int(input())

for _ in range(k):
  v,e = map(int, input().split())
  a = [[] for _ in range(v)]
  color = [0]*v

  for _ in range(e):
    x, y = map(int, input().split())
    a[x-1].append(y-1)
    a[y-1].append(x-1)

  def dfs(x, c):
    color[x] = c
    for y in a[x]:
      if color[y] == 0:
        if not dfs(y, 3-c):
          return False
      elif color[y] == color[x]:
        return False
    return True

  ans = True
  for i in range(v):
    if color[i] == 0:
      if not dfs(i, 1):
        ans = False
  print('Yes'if ans else 'No')

