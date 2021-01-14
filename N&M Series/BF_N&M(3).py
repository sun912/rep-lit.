#문제번호 : 15651

n, m = map(int, input().split())
if n > 8:
  quit()
a = [0]*m
# c = [False]*(n+1)

def go(index, n, m):
  if(index==m):
    print(' '.join(map(str,a)))
    return
  
  for i in range(1,n+1):
    # if c[i]:
      # continue
    a[index] = i
    # c[i] = True
    go(index+1,n,m)
    # c[i] = False

go(0,n,m)