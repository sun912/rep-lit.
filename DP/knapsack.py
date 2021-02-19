# BOJ 12865

n, k = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(n)]
w, v = zip(*temp)
w = [0] + list(w)
v = [0] + list(v)
d = [[0]*(k+1) for _ in range(n+1)]

#2array 
for i in range(1,n+1):
  for j in range(1,k+1):
    d[i][j] = d[i-1][j]
    if j-w[i] >= 0: 
      d[i][j] = max(d[i][j], d[i-1][j-w[i]] + v[i])

print(d[n][k])

#1array
# for i in range(1,n+1):
#   for j in range(k, 0, -1):
#     if j-w[i] >= 0:
#       d[j] = max(d[j], d[j-w[i]] + v[i])

# print(d[k])






