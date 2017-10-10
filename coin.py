# All Ways count

# def coun(arr, m, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if m <= 0 and n >= 1:
#         return 0
#     return coun(arr, m-1, n) + coun(arr, m, n-arr[m-1])

# min Way

def count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n+1)]
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n+1):
        for j in range(m):
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    return table[n][m-1]
    



def count(S, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j - S[i]]
        print(i)
        print(table)
    return table[n]