def a():
    nmk= input().strip().split()

    n,m,k = [int(a) for a in nmk]

    total = n*m
    tr = []
    su = 0
    oo = {}

    for i in range(k):
        r, s, e = [int(d) for d in input().strip().split()]
        lis = list(range(min(s,e) -1, max(s,e)))
        try:
            oo[r]
        except Exception:
            oo[r] = []
        for j in lis:
            oo[r].append(j)
    for k in oo:
        o = len(set(oo[k]))
        su += o

    print(total - su)


def merge(tups, min, max):
    tups.sort()
    tup = tups[-1]
    if min > tup[-1]:
        tups.append([min, max])
    if min <= tup[-1]:
        tup[-1] = max
    return tups




