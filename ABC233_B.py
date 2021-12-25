import io
import sys

_INPUT = """\
6
3 7
abcdefgh
1 7
reviver
4 13
merrychristmas
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L,R=map(int,input().split())
  S=input()
  ans=[]
  for i in range(len(S)):
    if L-1<=i<R:
      ans.append(S[L-2+R-i])
    else:
      ans.append(S[i])
  print(*ans,sep='')