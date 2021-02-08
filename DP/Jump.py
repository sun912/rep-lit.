#BOJ 1890 Jump 

#1st solution

# n = int(input())
# if n < 4:
#   quit()
# a = [list(map(int, input().split())) for _ in range(n)]
# d = [[0]*n for _ in range(n)]

# d[0][0] = 1

# for i in range(n):
#   for j in range(n):
#     if i == 0 and j == 0:
#       continue
#     for k in range(j):
#       if k + a[i][k] == j:
#         d[i][j] += d[i][k]
    
#     for k in range(i):
#       if k + a[k][j] == i:
#         d[i][j] += d[k][j]

# print(d[n-1][n-1])


#2nd solution

n = int(input())
if n < 4:
  quit()
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]

d[0][0] = 1

for i in range(n):
  for j in range(n):
    if a[i][j] == 0:
      continue
    if j + a[i][j] < n:
      d[i][j+a[i][j]] += d[i][j]
    
    if i + a[i][j] < n:
      d[i+a[i][j]] += d[i][j]

print(d[n-1][n-1])
