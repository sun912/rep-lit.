n,m = map(int,input().split())
if n > 8:
  quit()
nums = list(map(int, input().split()))
nums.sort()

a = [0]*m
c = [False]*n
def go(index,start,n,m):
  
  for i in range(start,n):
    if c[i]:
      continue
    if index == m:
      print(' '.join(map(str,a)))
      return
    c[i] = True
    a[index] = nums[i]
    go(index+1,i+1,n,m)
    c[i] = False

go(0,0,n,m)

