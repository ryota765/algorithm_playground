n = int(input())
matrix = [[l for l in input()] for i in range(n)]

# ブルートフォースO(N^2)
'''def func(n,matrix):
    return_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            return_matrix[j][n-1-i] = matrix[i][j]
    return return_matrix

for row in func(n,matrix):
    print(row)'''

# O(N)空間計算量削減
def func(n,matrix):
    for i in range(n):
        print([matrix[n-1-j][i] for j in range(n)])

func(n,matrix)

