# https://www.acmicpc.net/problem/1712

a,b,c = map(int,input().split())
if(c<=b or a//(c-b)<0):
  print(-1)
else:
  print(a//(c-b) + 1)