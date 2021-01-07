n, s = int(input().split())
if n < 1 or n > 20:
  quit()
nums = list(map(int,input().split()))
ans = 0

def go(i, sum):
  global ans
  if i == n:
    if sum == s:
      ans += 1
    return
  go(i+1,sum+nums[i])
  go(i+1,sum)

go(i = 0, sum = 0)
if s==0:
  ans -= 1
print(ans)


