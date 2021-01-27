#BOJ 2156

#점화식 나누어서 풀이
# n = int(input())
# a = list(int(input()) for _ in range(n))
# d = [[0]*3 for _ in range(n)]

# for i in range(n):
#   for j in range(3):
#     if j == 0:
#       d[i][j] = max(d[i-1])
#     if j == 1:
#       d[i][j] = d[i-1][0] + a[i]
#     if j == 2:
#       d[i][j] = d[i-1][1] + a[i]
# print(max(d[n-1]))

# 점화식 하나로 풀이
n = int(input())
a = [0] + list(int(input()) for _ in range(n))
d = [0] * (n+1)
d[1] = a[1]

if n>= 2:
  d[2] = a[1] + a[2]
for i in range(3,n+1):
  d[i] = d[i-1]
  d[i] = max(d[i],d[i-2]+a[i])
  d[i] = max(d[i],d[i-3]+a[i-1]+a[i])
print(d[n])