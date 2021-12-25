import io
import sys

_INPUT = """\
6
80 94
1000 63
270 750
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,Y=map(int,input().split())
  print(max(0,(Y-X-1)//10+1))