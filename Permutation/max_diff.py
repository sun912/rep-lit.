import sys


def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[i - 1] >= a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def calc(a):
  ans = 0
  for k in range(len(a)-1):
    ans += abs(a[k]-a[k+1])
  
  return ans

n = int(input())
if n > 8:
  exit()
  
a = list(map(int, input().split()))
ans = 0
a.sort()
# temp = 0
# while next_permutation(a):
#     for k in range(len(a)-1):
#         temp += abs(a[k] - a[k + 1])

#     if temp > total:
#         total = temp
#     temp = 0

"""==================="""
while True:
  temp = calc(a)
  ans = max(ans,temp)
  if not next_permutation(a):
    break
    
print(ans)
