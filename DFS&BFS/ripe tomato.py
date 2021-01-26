#BOJ 7576

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
a = [list(map(int, list(input().split()))) for _ in range(m)]
dist = [[-1]*n for _ in range(m)]
q = deque()

for i in range(m):
  for j in range(n):
    if a[i][j] == 1 and dist[i][j] == -1:
      q.append((i,j))  
      dist[i][j] = 0

while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < m and 0 <= ny < n:
      if a[nx][ny] == 0 and dist[nx][ny] == -1:        
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))      
    
ans = max([max(row) for row in dist])
for i in range(m):
  for j in range(n):
    if dist[i][j] == -1 and a[i][j] == 0:
      ans = -1

print(ans)





        








