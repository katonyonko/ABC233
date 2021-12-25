import io
import sys

_INPUT = """\
6
1225
99999
314159265358979323846264338327950288419716939937510
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=input()
  N=len(X)
  tmp=[0]
  for i in range(N):
    tmp.append(tmp[-1]+int(X[i]))
  tmp=tmp[1:]
  tmp=tmp[::-1]
  for i in range(N-1):
    tmp[i+1]+=tmp[i]//10
    tmp[i]=tmp[i]%10
  tmp=tmp[::-1]
  print(*tmp,sep='')