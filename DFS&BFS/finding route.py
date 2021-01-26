#BOJ 4963
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
dist = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
q = deque()
q.append((0,0))
check[0][0] = True
dist[0][0] = 1

while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 1 and check[nx][ny] == False:
        q.append((nx,ny))
        check[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])
        








