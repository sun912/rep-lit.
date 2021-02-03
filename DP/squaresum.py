#BOj 1699

n = int(input())
d = [0]*(n+1)   #제곱수의 합으로 나타낼 때 항의 최소 갯수

for i in range(1,n+1):
  d[i] = i
  j = 1
  while j*j <= i:
    if d[i] > d[i-j*j] + 1:
      d[i]  = d[i-j*j] + 1 
    j += 1
print(d[n])