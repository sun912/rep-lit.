# BOJ 2294  
n, m = map(int,input().split())
values = [int(input()) for _ in range(n)]
d = [-1]*(m+1)
d[0] = 0
for value in values:
  for j in range(m+1):
    if j - value >= 0 and d[j-value] != -1:
      if d[j] == -1 or d[j] > d[j-value] + 1:
        d[j] = d[j-value] + 1 
print(d[m])

  
  