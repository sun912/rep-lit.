def next_permutation(a):
  i = len(a)-1
  while i>0 and a[i-1] >= a[i]:
    i -= 1
  
  if i<=0:
    return False
  
  j = len(a)-1
  while a[i-1] >= a[j]:
    j -= 1
  a[i-1], a[j] = a[j], a[i-1]

  j = len(a)-1
  while i>j:
    a[i],a[j] = a[j],a[i]
    i += 1
    j -= 1
  
  return True

n = int(input())
if n > 8:
    exit()
a = [k for k in range(1,n+1)]
print(' '.join(map(str,a)))
while next_permutation(a):
  np = a
  print(' '.join(map(str,np)))