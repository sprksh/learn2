def r():

    nq = input().strip()
    n, q = int(nq.split()[0].strip()), int(nq.split()[1].strip())

    dic = {0: [], 1: []}
    last_answer = 0

    for i in range(0, q):
        inp = input()
        seq_str = inp.strip().split()
        s = [int(a) for a in seq_str]
        b = (bool(s[1]) ^ bool(last_answer)) % n
        print('b: {}'.format(b))
        if s[0] == 1:
            dic[b].append(s[-1])
        elif s[0] == 2:
            position = s[-1] % len(dic[b])
            last_answer = dic[b][position]

            print(last_answer)
        print(dic[0], dic[1])


# def f():
# for i in range(1,5):
#     print(int(i*'1')**2)
    

def wonder(s):
    try:
        if int(s) % 2:
            val = int(s) + 500
        else:
            val = int(s) + 1000
    except Exception:
        if s.islower():
            val = ord(s)
        else:
            val = ord(s) + 100
    return val
w =  sorted(s, key=wonder)
print(*w, sep='')


def capitalize(string):
    ss = string.split(' ')
    new_s = []
    for s in ss:
        c = s[0].upper() + s[1:]
        new_s.append(c)
    return ' '.join(new_s)

# def rangoli():
a = 5
for i in reversed(list(range(a))):
    for j in range(a):

alphs = 'abcdefghijklmnopqrstuvwxyz'

n = 5
b = (2*n) -1
for i in range(b):
    lis = []
    for j in reversed(list(range(b))):
        z = min(abs(b-i), i)
        y = min(b-j, j)
        var = '-'
        if j in range((n-1)-z, n+z):
            var = alphs[max(abs(j-i), abs(i-j))]
        lis.append(var)
    print(lis)
            