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
6
5 2 3 1 4 6
4
1 3
5 6
1 4
2 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  N=int(input())
  P=list(map(lambda x:int(x)-1,input().split()))
  Q=[-1]*N
  for i in range(N):
    Q[P[i]]=i
  M=int(input())
  uf=UnionFind(N)
  G=[[] for _ in range(N)]
  c={}
  swap=[None]*M
  flg=0
  for i in range(M):
    a,b=map(lambda x:int(x)-1,input().split())
    if uf.find(a)!=uf.find(b):
      uf.union(a,b)
      G[a].append(b)
      G[b].append(a)
      c[(a,b)]=i
      swap[i]=(a,b)
  used=[0]*N
  depth=[0]*N
  parents=[-1]*N
  ans=[]
  for i in range(N):
    if used[i]==1: continue
    used[i]=1
    dq=deque([i])
    while dq:
      x=dq.popleft()
      for v in G[x]:
        if used[v]==0:
          used[v]=1
          depth[v]=depth[x]+1
          parents[v]=x
          dq.append(v)
    tmp=sorted([(j,depth[j]) for j in uf.members(i)],key=lambda x:-x[1])
    tmp2=set([tmp[j][0] for j in range(len(tmp))])
    for j in range(len(tmp)):
      k=tmp[j][0]
      if P[k] not in tmp2: flg=1; break
    if flg==1: break
    for j in range(len(tmp)):
      k,l=tmp[j][0],Q[tmp[j][0]]
      tmp3=[]
      tmp4=[]
      if depth[k]>depth[l]:
        for p in range(depth[k]-depth[l]):
          tmp3.append(c[(min(k,parents[k]),max(k,parents[k]))])
          k=parents[k]
      if depth[k]<depth[l]:
        for p in range(depth[l]-depth[k]):
          tmp4.append(c[(min(l,parents[l]),max(l,parents[l]))])
          l=parents[l]
      while k!=l:
        tmp3.append(c[(min(k,parents[k]),max(k,parents[k]))])
        tmp4.append(c[(min(l,parents[l]),max(l,parents[l]))])
        k=parents[k]
        l=parents[l]
      for p in range(len(tmp4)):
        ans.append(tmp4[p])
        a,b=swap[tmp4[p]]
        P[a],P[b]=P[b],P[a]
        Q[P[a]],Q[P[b]]=Q[P[b]],Q[P[a]]
      for p in reversed(range(len(tmp3))):
        ans.append(tmp3[p])
        a,b=swap[tmp3[p]]
        P[a],P[b]=P[b],P[a]
        Q[P[a]],Q[P[b]]=Q[P[b]],Q[P[a]]
  if flg==1: print(-1)
  else:
    print(len(ans))
    print(*[ans[i]+1 for i in range(len(ans))])