import io
import sys

_INPUT = """\
6
2 40
3 1 8 4
2 10 5
3 200
3 10 10 10
3 10 10 10
5 2 2 2 2 2
3 1000000000000000000
2 1000000000 1000000000
2 1000000000 1000000000
2 1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import itertools
  N,X=map(int,input().split())
  balls=[]
  for i in range(N):
    ball=list(map(int,input().split()))
    balls.append(ball[1:])
  ans=0
  result = list(itertools.product(*balls))
  for k in result:
    tmp=1
    for i in range(N):
      tmp*=k[i]
    if tmp==X:
      ans+=1
  print(ans)