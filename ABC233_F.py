import io
import sys

_INPUT = """\
6
6
5 3 2 4 6 1
4
1 5
5 6
1 2
2 3
5
3 4 1 2 5
2
1 3
2 5
4
1 2 3 4
6
1 2
1 3
1 4
2 3
2 4
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  P=list(map(int,input().split()))
  P=[P[i]-1 for i in range(N)]
  M=int(input())
  G=[[] for _ in range(N)]
  dic=dict()
  for i in range(M):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)
    dic[(a,b)]=i+1
  dir=[]
  used=[-1]*N
  for i in range(N):
    if used[i]==0: continue
    tmp=[i]
    now=P[i]
    while now!=i:
      used[now]=0
      tmp.append(now)
      now=P[now]
    dir.append(tmp)
  K=0
  ans=[]
  used=[-1]*N
  parent=[-2]*N
  inf=10**30
  D=[inf]*len(G)
  from collections import deque
  def bfs(G,s):
    D[s]=0
    parent[s]=-1
    dq=deque()
    dq.append(s)
    used[s]=0
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
          parent[y]=x
          used[y]=0

  for i in range(N):
    if used[i]==0: continue
    bfs(G,i)
    l=len(dir[i])
    for j in range(l):
      dir[i][j], dir[i][(j+1)%l]