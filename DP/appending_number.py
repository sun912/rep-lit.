# BOJ 1748

n = int(input())
start = 1
length = 1
ans = 0

while start <= n:           #입력한 수 보다 자리수가 작을 때까지만 실행
    end = start * 10 - 1    #끝자리 수 
    if n < end:             # 입력수의 자리 수 찾기
        end = n
    ans += (end-start+1)*length   #글자 수 count
    length += 1                   
    start *= 10
print(ans)

