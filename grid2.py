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



n = input().strip()
a = [int(x_temp) for x_temp in input().strip().split(' ')]


    n = int(input().strip())

    grid = []
    sorted_grid = []
    for i in range(n):
        row = [i for i in input().strip()]
        grid.append(row)

    for i in grid:
        si = sorted(i, key=ord)
        sorted_grid.append(si)

    val = 'YES'
    for i in range(n):
        col = []
        col.append(sorted_grid[i][0])
        sorted_col = sorted(col, key=ord)
        if sorted_col == col:
            pass
        else:
            val = 'NO'
            break
    print(val)



n = input().strip()
a = [int(x_temp) for x_temp in input().strip().split(' ')]

result = 0

for i, x in enumerate(a):
    for j, y in enumerate(a[i + 1:]):
        if ((x + y) in a):
            result += 1

print(result)