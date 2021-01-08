n,m = map(int,input().split())
if n > 8:
  quit()
t = list(map(int, input().split()))
c = [False]*n
a = [0]*m
t.sort()

def go(index,n,m):
  if index == m:
    print(' '.join(map(str,a)))
    return

  for i in range(n):
    if c[i]:
      continue
    a[index] = t[i]
    c[i] = True
    go(index+1,n,m)
    c[i] = False
    
go(0,n,m)