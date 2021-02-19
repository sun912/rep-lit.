# BOJ 1748

n = int(input())
start = 1
length = 1
ans = 0
while start <= n:
    end = start * 10 - 1
    if n < end:
        end = n
    ans += (end-start+1)*length
    length += 1
    start *= 10
print(ans)

