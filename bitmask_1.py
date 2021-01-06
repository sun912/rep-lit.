import sys

n = 20
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
  op, *num = sys.stdin.readline().split()
  if len(num) > 0:
    x = int(num[0])-1
  if op == 'add':
    s = (s | (1 << x))
  elif op == 'remove':
    s = (s & ~(1 << x))
  elif op == 'check':
    if (s & (1<<x)):
      sys.stdout.write('1\n')
    else:
      sys.stdout.write('0\n')
  elif op == 'all': 
    s = (1 << n)-1
  elif op == 'toggle':
    s = (s ^ (1<<x))
  else:
    s = 0
  


