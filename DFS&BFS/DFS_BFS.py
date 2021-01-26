from collections import deque
v,e,start = map(int,input().split())
a = [[] for _ in range(v+1)]
c = [False]*(v+1)

for _ in range(e):
  u,v = map(int, input().split())  
  a[u].append(v)
  a[v].append(u)
for i in range(v):
  a[i].sort()

def DFS(x):
  global check
  c[x] = True
  print(x, end = ' ')

  for i in a[x]:
    if c[i] == False:
      DFS(a[i])

def BFS(start):
  check = [False]*(v+1)
  q = deque()
  q.append(start)
  check[start] = True
  while q:
    x = q.popleft()
    print(x, end = ' ')
    for y in a[x]:
      if check[y] == False:
        check[y] = True
        q.append(y)

DFS(start)
print()
BFS(start)
print()

