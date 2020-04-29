import sys

n = int(input())
a_list = list(map(int,input().split()))
k = int(input())

print(n,a_list,k)

def DFS(k,unused_list,used_list):
    if sum(used_list) < k:
        for elem in unused_list:
            used_list.append(elem)
            del unused_list[unused_list.index(elem)]
            DFS(k,unused_list,used_list)
    elif sum(used_list) == k:
        print('yes')
        sys.exit()

DFS(k,a_list,[])

print('no')


        