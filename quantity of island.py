#BOJ 4963

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,cnt):
  q = deque()
  q.append((x,y))
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and  0 <= ny <m:
      if a[nx][ny] == 1 and group[nx][ny] == 0:
        q.append((nx,ny))
        group[nx][ny] = cnt

while True:
  n,m = map(int,input().split())
  if  n == 0 and m == 0:
    break
  a = [list(map(int,input().split('',m))) for _ in range(n)]
  group = [[0]*m for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(m):
      if a[i][j] == 1 and group[i][j] == 0:
        cnt += 1
        bfs(i,j,cnt)



