import sys

n,m = map(int,input().split())
cnt = [0]*(n+1)
if n > 8:
  quit()

def go(index,selected,m,n):
  if selected == m:
    for i in range(1,n+1):
      for j in range(cnt[i]):
        sys.stdout.write(str(i)+ ' ')
    sys.stdout.write('\n')
    return
  if index > n:
    return
  for i in range(m-selected,0,-1):
    cnt[index] = i
    go(index+1,selected+i,m,n)
  cnt[index] = 0
  go(index+1,selected,m,n)  

go(1,0,m,n)