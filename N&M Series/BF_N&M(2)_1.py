n, m = map(int,input().split())
if n > 8:
  quit()
a = [0]*m

def go(index,s,n,m):
  if s == m:
    print(' '.join(map(str,a)))
    return

  if index > n:
    return
  a[s] = index
  go(index+1,s+1,n,m)
  a[s] = 0
  go(index+1,s,n,m)

go(1,0,n,m)
   