import sys
n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
if n>7:
  quit()

a = [0]*m
c = [False]*n

def go(index,start,m,n):
  if index == m:
    sys.stdout.write(' '.join(map(str,a))+'\n')
    return
  if index > n:
    return

  for i in range(start,n):
    c[i] = True
    a[index] = nums[i]
    go(index+1,i,m,n)
    c[i] = False
  
go(0,0,m,n)
