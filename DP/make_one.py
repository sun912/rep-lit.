#BOJ 1463


#Top down solving
import sys
sys.setrecursionlimit(10000000)
n = int(input())
d = [0]*(n+1)
# def go(x):
#   if x == 1:
#     return 0
#   if d[x] > 0:
#     return d[x]
#   d[x] = go(x-1) + 1
#   if x % 2 == 0:
#     temp = go(x//2) + 1
#     if d[x] > temp:
#       d[x] = temp
#   if x% 3 == 0:
#     temp = go(x//3) + 1
#     if d[x] > temp:
#       d[x] = temp
#   return d[x]

# d = [0]*(n+1)
# print(go(n))


#Bottom up 
d[1] = 0
for i in range(2,n+1):
  d[i] = d[i-1]+1
  if i % 2 == 0 and d[i] > d[i//2]+1:
    d[i] = d[i//2] + 1
  if i % 3 == 0 and d[i] > d[i//3]+1:
    d[i] = d[i//3] + 1
print(d[n])



