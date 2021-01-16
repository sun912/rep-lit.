import sys
sys.setrecursionlimit(100000)

v,e = map(int, input().split())
a = [[] for _ in range(v)]
c = [False]*(v)

for _ in range(e):
  x, y = map(int, input().split())
  a[x-1].append(y-1)
  a[y-1].append(x-1)

for i in range(v):
  a[i].sort()

def dfs(x):
  c[x] = True
  for i in a[x]:
    if c[i] == False:
      dfs(i)

ans = 0
for i in range(v):
  if not c[i]:
    dfs(i)
    ans += 1

print(ans)
