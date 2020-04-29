import numpy as np

n,m = map(int,input().split())
data = [list(input()) for _ in range(n)]

def delete_surrounding(lake,point):
    lake[point[0]][point[1]] = '.'
    y_start = point[0]-1
    y_end = point[0]+1
    x_start = point[1]-1
    x_end = point[1]+1
    if point[0] == 0:
        y_start = 0
    elif point[0] == n:
        y_end = n-1
    if point[1] == 0:
        x_start = 0
    elif point[1] == m:
        x_end = m-1
    target = np.array(lake)[y_start:y_end+1,x_start:x_end+1].tolist()
    for i in range(len(target[0])):
        for j in range(len(target)):
            if lake[y_start+j][x_start+i] == '#':
                point_new = [y_start+j,x_start+i]
                delete_surrounding(lake,point_new)
    return lake

count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            count += 1
            data = delete_surrounding(data,[i,j])

print(count)

'''
10 5
.....
##...
#....
..###
...##
.#...
.....
##...
...##
.....
'''