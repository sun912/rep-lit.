# BOJ 10942


# using recursive function
# import sys
# sys.setrecursionlimit(100000)
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())

# d = [[-1]*n for _ in range(n)]

# def go(i,j):
#   if i == j:
#     return 1
#   elif i+1 == j:
#     if a[i] == a[j]:
#       return 1
#     else:
#       return 0
#   if d[i][j] != -1:
#     return d[i][j]

#   if a[i] != a[j]:
#     d[i][j] = 0
#   else:
#     d[i][j] = go(i+1,j-1)
#   return d[i][j]

# for _ in range(m):
#   s,e  = map(int, sys.stdin.readline().split())
#   print(go(s-1,e-1))

# using for loop
# for loop start, end point 정하는게 이해가 되지 않음
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
d = [[-1]*n for _ in range(n)]

for i in range(n):
  d[i][i] = True
for i in range(n-1):
  if a[i] == a[i+1]:
    d[i][i+1] = True

for k in range(3,n+1):      #시작위치
  for i in range(0,n-k+1):  #길이
    j = i+k-1
    if a[i] == a[j] and d[i+1][j-1]:
      d[i][j] = True

for _ in range(m):
  s,e = map(int, sys.stdin.readline().split())
  print(1 if d[s-1][e-1] else 0)






  