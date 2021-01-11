n,m = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
if n>7:
  quit()

a = [0]*m
def go(index,m,n):
  if index == m:
    print(' '.join(map(str,a)))
    return
  if index > n:
    return
  
  for i in range(n):
    a[index] = nums[i]
    go(index+1,m,n)
    

  return

go(0,m,n)
