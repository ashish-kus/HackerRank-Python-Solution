m=int(input())
m_list=set(map(int,input().split()))
n=int(input())
n_list=set(map(int,input().split()))

o=m_list.intersection(n_list)
for i in sorted(n_list.difference(o).union(m_list.difference(o))):
    print(i)

