from collections import deque
v, e, s = map(int,input().split())
a = [[] for _ in range(e)]
c = [False]*(v+1)
for _ in range(e):
  u,v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)
for i in range(v):
  a[i].sort()

def dfs(x):
  global c
  c[x] = True
  print(x, end=' ')
  for y in a[x]:
    if c[y] == False:
      dfs(y)
    
def bfs(x):
  c = [False]*(v+1)
  q = deque()
  q.append(s)
  c[s] = True
  while q:
    x = q.popleft()
    print(x, end = ' ')
    for y in a[x]:
      if c[y] == False:
        c[y] = True
        q.append(y)

dfs(s)
print()
bfs(s)
print()


