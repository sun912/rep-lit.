#BOJ 6064

t = int(input())

for _ in range(t):
    m,n,x,y = list(map(int, input().split()))
    x -= 1
    y -= 1
    k = x
    while k < m*n:
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)


