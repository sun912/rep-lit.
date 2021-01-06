n, s = map(int, input().split())
numbers = list(map(int,input().split()))
ans = 0

for i in range(1,(1<<n)):
  m = sum(numbers[k] for k in range(n) if (i &(1<<k))>0 )

  if m == s:
    ans += 1

print(ans)