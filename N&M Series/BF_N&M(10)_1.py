import sys

n,m = map(int,input().split())
if n > 8:
  quit()
nums = list(map(int, input().split()))
nums.sort()

a = [0]*m
c = [False]*n
d = []

def go(index,start,n,m):
  if index == m:
      d.append(tuple(a))
      return
  for i in range(start,n):
    if c[i]:
      continue
    
    c[i] = True
    a[index] = nums[i]
    go(index+1,i+1,n,m)
    c[i] = False

go(0,0,n,m)
d = sorted(list(set(d)))
for v in d:
  sys.stdout.write(' '.join(map(str,v))+'\n')



