n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

data = sorted(data, key=lambda x: x[1])
time = 0
count = 0

for d in data:
    if d[0] >= time:
        time = d[1]
        count += 1
    
print(count)