#BOj 11054

#a[i]를 시작으로 작아지는 수열, a[i]를 끝으로 하는 부분수열의 값을 구하고 더한 후 최댓값을 구함


n = int(input())
a = list(map(int, input().split()))
d1 = [0]*n
d2 = [0]*n
for i in range(n):
  d1[i] = 1
  for j in range(i):
    if a[i] > a[j] and d1[i] < d1[j]+1:
      d1[i] = d1[j] + 1

for i in range(n-1,-1,-1):
  d2[i] = 1
  for j in range(i+1,n):
    if a[i] > a[j] and d2[i] < d2[j]+1:
      d2[i] = d2[j]+1

d = [d1[i] + d2[i]-1 for i in range(n)]
print(max(d))

