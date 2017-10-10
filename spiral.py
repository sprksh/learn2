def dfs(matrix, cache, i, j, n):
    directions = [(1,0), (-1,0), (0,-1), (0,1)]
    if cache[i][j] > -1:
        return cache[i][j]

    res = 1
    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] == '0':
            cache[x][y] = 0
            continue
        length = 1 + dfs(matrix, cache, x, y, n)
        res = max(length, res)
    cache[i][j] = res
    return res


def lands(matrix):
    if not matrix:
        return 0
    cache = [[-1 for _ in mat] for _ in mat]
    res = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            cur_len = dfs(matrix, cache, i, j, n)
            res = max(res, cur_len)
    print(res)

mat = []
for j in range(4):
    a_mat = [i for i in input().split()]
    mat.append(a_mat)
lands(mat)
