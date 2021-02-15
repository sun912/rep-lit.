# BOJ 11058

n = int(input())
d = [0]*(n+1)
for i in range(1,n+1):
  d[i] = d[i-1] + 1           #A를 추가하는 버튼을 눌렀을 때
  for j in range(1, i-3+1):   #ctrl + v를 누른 횟수에 따라 비교할 때
    cur = d[i-j-2]*(j+1)
    if cur > d[i]:
      d[i] = cur
print(d[n])