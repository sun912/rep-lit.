#15652

n, m = map(int, input().split())
if n > 8:
  quit()
a = [0]*m
# c = [False]*(n+1)

def go(index, start, n, m):
  if(index==m):
    print(' '.join(map(str,a)))
    return
  
  for i in range(start,n+1):
    # if c[i]:
      # continue
    a[index] = i
    # c[i] = True
    go(index+1,i,n,m)
    # c[i] = False

go(0,1,n,m)