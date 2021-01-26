# #BOJ 13549

from collections import deque
MAX = 200000
check = [False]*MAX
dist = [-1]*MAX
n,k = map(int, input().split())
q = deque()
nxt_q = deque()
check[n] = True
dist[n] = 0
q.append(n)

while q:
  now = q.popleft()
  if now*2 < MAX and check[now*2] == False:
    q.appendleft(2*now)
    check[2*now] = True
    dist[2*now] = dist[now]
  if now+1 < MAX and check[now+1] == False:
    nxt_q.append(now+1)
    check[now+1] = True
    dist[now+1] = dist[now] + 1
  if now-1 >= 0 and check[now-1] == False:
    nxt_q.append(now-1)
    check[now-1] = True
    dist[now-1] = dist[now] + 1
  if not q:
    q = nxt_q
    nxt_q = deque()

print(dist[k])
        








