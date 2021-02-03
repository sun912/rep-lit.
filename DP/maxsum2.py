#BOj 13398

n = int(input())
a = list(map(int, input().split()))
dl = [0]*n
dr = [0]*n
for i in range(n):
  dl[i] = a[i]
  if i == 0:
    continue
  if dl[i] < dl[i-1] + a[i]:
    dl[i] = dl[i-1] + a[i]

for i in range(n-1,-1,-1):
  dr[i] = a[i]
  if i == n-1:
    continue
  if dr[i] < dr[i+1] + a[i]:
    dr[i]  = dr[i+1] + a[i]

ans = max(dl)
for i in range(1,n-1):
  if ans < dl[i-1] + dr[i+1]:
    ans = dl[i-1] + dr[i+1]
  
print(ans)

