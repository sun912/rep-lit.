#BOJ 11722 Longest decreasing subsequence

n = int(input())
a = list(map(int, input().split()))
d = [0]*n

# 시작점을 기준으로 감소하는 방식으로 부분수열 구하기
# for i in range(n-1,-1,-1):
#   d[i] = 1
#   for j in range(i+1,n):
#     if a[i] > a[j] and d[i] < d[j] + 1:
#       d[i] = d[j] + 1
# print(max(d))

#수열을  flip해서 증가하는 부분 수열의 최대수 구하는법
# for i in range(n):
#   d[i] = 1
#   for j in range(i):
#     if a[i] < a[j] and d[i] < d[j]+1:
#       d[i] = d[j]+1
# print(max(d))

for i in range(n):
  d[i] = 1
  for j in range(i):
    if a[i] < a[j] and d[i] < d[j] + 1:
      d[i] = d[j] + 1
print(max(d))
