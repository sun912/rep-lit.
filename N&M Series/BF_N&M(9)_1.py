import sys

n,m = map(int,input().split())
if n > 8:
  quit()
t = list(map(int, input().split()))
c = [False]*n
a = [0]*m
t.sort()
d = []
def go(index,n,m):
  if index == m:
    d.append(tuple(a))
    return

  for i in range(n):
    if c[i]:
      continue
    a[index] = t[i]
    c[i] = True
    go(index+1,n,m)
    c[i] = False
    
go(0,n,m)
d = sorted(list(set(d)))
for v in d:
  sys.stdout.write(' '.join(map(str,v))+'\n')
