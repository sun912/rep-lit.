#make lottery number using recursive function
def go(numbers, i, num_set):
  if len(num_set) == 6:
    print(' '.join(map(str,num_set)))
    return

  if i == len(numbers):
    return

  go(numbers,i+1,num_set+[numbers[i]])
  go(numbers,i+1,num_set)


  #2. cnt > n
  #3. cnt < n

while True:
  n, *numbers = list(map(int, input().split()))
  if n > 13 or n < 6:
    break
  # numbers.sort()
  go(numbers,0,[])
  print()