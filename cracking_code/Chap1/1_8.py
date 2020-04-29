m = int(input()) 
n = int(input())
matrix = [list(map(int,input())) for i in range(n)]

# O(N^2)プルートフォース
'''
def func(m,n,matrix):
    return_matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        if 0 in [matrix[j][i] for j in range(n)]:
            for k in range(n):
                return_matrix[k][i] = 0
        else:
            for k in range(n):
                return_matrix[k][i] = matrix[k][i]   
    for i in range(n):
        if 0 in matrix[i]:
            return_matrix[i] = [0 for j in range(m)]
        else:
            for j in range(len(matrix[i])):
                if return_matrix[i][j] == 0:
                    pass
                else:
                    return_matrix[i][j] = matrix[i][j]
    return return_matrix
    '''

# O(N)空間計算量削減
def func(m,n,matrix):
    row = [False for i in range(m)]
    col = [False for i in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[j] = True
                col[i] = True
    print(row,col)
    for i,b in enumerate(row):
        if b == True:
            for j in range(n):
                matrix[j][i] = 0
    for i,b in enumerate(col):
        if b == True:
            matrix[i] = [0 for i in range(m)]
    return matrix

print(func(m,n,matrix))