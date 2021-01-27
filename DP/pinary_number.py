#BOJ 2193 Pinary number

#using 1st array
# n = int(input())
# d = [0]*91
# d[1] = 1
# d[2] = 1
# for i in range(3,n+1):
#   d[i] = d[i-1] + d[i-2]
# print(d[n])

#using 2nd array
n = int(input())
d = [[0]*91 for _ in range(n+1)]
d[1][0] = 0
d[1][1] = 1
for i in range(2,n+1):
  for j in range(2):
    if j == 0:
      d[i][j] = d[i-1][0] + d[i-1][1]
    if j == 1:
      d[i][j] = d[i-1][0]
  
print(sum(d[n]))
