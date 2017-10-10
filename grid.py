# nmk= input().strip().split()

# n,m,k = [int(a) for a in nmk]

# total = n*m
# tr = []
# su = 0
# oo = {}

def merge(times):
    ss = sorted([sorted(t) for t in times])
    saved = list(ss[0])
    for st, en in ss[1:]:
        if st <= saved[1]:
            saved[1] = max(saved[1], en)
        else:
            yield tuple(saved)
            saved[0] = st
            saved[1] = en
    yield tuple(saved)

# for i in range(k):
#     r, s, e = [int(d) for d in input().strip().split()]
    
#     if not oo.get(r, 0):
#         oo[r] = [(s,e)]
#     else:
#         oo[r].append((s,e))
        
# for k in oo:
#     tups = oo[k]
#     for u in list(merge(tups)):
#         su += (u[-1] - u[0]) + 1


n = input().strip()
a = [int(x_temp) for x_temp in input().strip().split(' ')]


def fract(i):
    d = 9
    while d < i:
        d = 10 * d + 9
    return i / d

sorted_a = sorted(a, key=fract, reverse=True)

str_a = [str(i) for i in sorted_a]

print(''.join(str_a))


#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value

    answer = 0
    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))