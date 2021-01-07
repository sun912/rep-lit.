def check(pwd):
  ja = 0
  mo = 0

  for j in pwd:
    if j in 'aeiou':
      mo += 1
    else:
      ja += 1
  return ja >= 2 and mo >= 1

def go(n,alpha,passwd,i):  
  
  if len(passwd) == n:    
    if check(passwd):
      print(passwd)
    return

  if i == len(alpha):
    return 

  go(n,alpha, passwd+alpha[i], i+1)
  go(n,alpha, passwd, i+1)


n, L = map(int, input().split())
alpha = input().split()
if len(alpha) > 15:
  quit()
alpha.sort()
pwd = ''
go(n,alpha,pwd,0)


