import io
import sys

_INPUT = """\
6
6 5
8 -3 5 7 0 -4
2 -1000000000000000
1000000000 -1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  acc=[0]
  for i in range(N):
    acc.append(acc[-1]+A[i])
  acc=acc[1:]
  cnt=defaultdict(int)
  for i in range(N):
    cnt[acc[i]]+=1
  ans=0
  for i in range(N):
    ans+=cnt[K]
    cnt[acc[i]]-=1
    K+=A[i]
  print(ans)