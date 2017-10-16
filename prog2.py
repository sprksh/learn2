# prog2.py


mat = []
m, n = len(mat), len(mat[0])
directions = [(0,1),(1,0)]

start = [0,0]
target = [m-1, n-1]
tem = []
val = 1


def dfs(mat, target, i, j):
    
    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if [ni, nj] == target:
            return
        if mat[i][j]
        
    


