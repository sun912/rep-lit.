def go(a,i,cur,plus,minus,mul,div):
  



n = int(input())
nums = list(map(int, input().split()))
plus,minus,mul,div = list(map(int, input().split()))

go(nums,0,0,plus,minus,mul,div)
