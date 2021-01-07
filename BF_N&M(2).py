import sys

n, m = map(int, input().split())
if n > 8:
  quit()
a = [0]*m

def go(index,start, n, m):
  if(index==m):
    print(' '.join(map(str,a)))
    return
  
  for i in range(start,n+1):
    if i > a[start]:
      a[index] = i
    go(index+1,i+1,n,m)
                            
go(0,1,n,m)
