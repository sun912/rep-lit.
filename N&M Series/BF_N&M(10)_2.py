import sys
from collections import Counter

n,m = map(int,input().split())
temp = list(map(int,input().split()))
temp = list(Counter(temp).items())
temp.sort()
n = len(temp)
num,cnt = map(list,zip(*temp))
a = [0]*m

def go(index,start,n,m):
  if index == m:
    sys.stdout.write(' '.join(map(str,a))+'\n')
    return
  for i in range(start,n):
    if cnt[i] > 0:
      cnt[i] -= 1
      a[index] = num[i]
      go(index+1,i,n,m)
      cnt[i] += 1
go(0,0,n,m)

