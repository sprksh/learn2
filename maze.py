def check(mat, i, j, n):
    if i < 0 or j < 0 or i >= n or j >= n or mat[i][j] == 0:
        return False
    return True

def find(mat, i, j, n, sol, target):
    if (i, j) == target:
        sol[i][j] = 1
        return True

    if check(mat, i, j, n):
        sol[i][j] = 1

        ds = [(1,0), (0, 1), (-1, 0), (0, -1)]

        if find(mat, i+1, j, n, sol, target):
            return True
        if find(mat, i, j+1, n, sol, target):
            return True
        if find(mat, i-1, j, n, sol, target):
            return True
        if find(mat, i, j-1, n, sol, target):
            return True
        # for d in ds:
        #     i, j = i + d[0], j + d[1]
        #     if find(mat, i, j, n, sol, target):
        #         return True
        sol[i][j] = 0
        return False
    return False


####################################

mat = []

for j in range(6):
    a_mat = [int(i) for i in input().split()]
    mat.append(a_mat)
n = len(mat)
sol = [[0 for _ in range(n)] for _ in range(n)]
if find(mat, 0, 0, n, sol, (n-1, n-1)):
    for i in range(n):
        print(sol[i])


'''
1 1 0 1 1
0 1 1 1 1
0 0 0 0 1
1 0 1 1 1
1 0 1 0 1

1 0 1 1 1 0
1 0 1 0 1 0
1 0 1 0 1 0
1 0 1 0 1 0
1 1 1 0 1 1
0 0 0 0 0 1
'''
