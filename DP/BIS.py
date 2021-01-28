#BOJ 11055 가장 큰 증가 부분 수열

n = int(input())
a = list(map(int, input().split()))
d = [0]*n
v = [-1]*n
for i in range(n):
  d[i] = 1
  for j in range(i):
    if a[j] < a[i] and d[j]+a[i] > d[i]:
      d[i] = d[j]+a[i]
      

ans = max(d)

print(ans)







# 1 100 2 50 60 3 5 6 7 8