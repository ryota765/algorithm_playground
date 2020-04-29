'''graph = [
    ['a','b'],
    ['a','c'],
    ['c','d'],
    ['d','e'],
    ['d','f'],
    ['f','g']
]'''
import sys

graph = {
    'a': ['c'],
    'b': ['c','f'],
    'c': ['a','b','d'],
    'd': ['e','f'],
    'e': ['d'],
    'f': ['b','d','g'],
    'g': ['f']
}

# queueの実装
class Queue:
    def __init__(self):
        self.queue = []
    # 先頭にデータを追加
    def add(self,x):
        self.queue.append(x)
    # 最後のデータを削除
    def remove(self):
        del self.queue[0]
    # 最後のデータを返す
    def peek(self):
        return self.queue[0]
    # queueをprint
    def get_queue(self):
        print(self.queue)
    # 空かどうか確認
    def is_empty(self):
        return len(self.queue) == 0


# 深さ優先探索
def DFS(graph,start,end,mark_dict):
    mark_dict[start] = True
    for target in graph[start]:
        if target == end:
            print('Exist')
            sys.exit()
        elif target not in mark_dict:
            mark_dict[target] = True
            DFS(graph,target,end,mark_dict)


# 幅優先探索
def BFS(graph,start,end):
    mark_dict = {}
    queue = Queue()
    queue.add(start)
    while queue.is_empty() == False:
        target = queue.peek()
        queue.remove()
        if target not in mark_dict:
            mark_dict[target] = True
            if target != end:
                for elem in graph[target]:
                    queue.add(elem)
            else:
                print('Exist')
                sys.exit()

# 双方向探索のためのフラグ付きqueueの実装
class FlagQueue:
    def __init__(self):
        self.queue = []
    # 先頭にデータを追加
    def add(self,x,flag):
        self.queue.append([x,flag])
    # 最後のデータを削除
    def remove(self):
        del self.queue[0]
    # 最後のデータを返す
    def peek(self):
        return self.queue[0]
    # queueをprint
    def get_queue(self):
        print(self.queue)
    # 空かどうか確認
    def is_empty(self):
        return len(self.queue) == 0

# 双方向探索
def BidirectionalSearch(graph,start,end):
    mark_dict = {0: {},1: {}}
    queue = FlagQueue()
    queue.add(start,0)
    queue.add(end,1)
    while queue.is_empty() == False:
        target = queue.peek()
        queue.remove()
        # 'target'が反対側のdictionaryで既出
        if target[0] in mark_dict[1-target[1]]:
            print('Exist')
            sys.exit()
        # 'target'が自分側のdictionaryで未出
        elif target[0] not in mark_dict[target[1]]:
            mark_dict[target[1]][target[0]] = True
            for elem in graph[target[0]]:
                queue.add(elem,target[1])


# BFS(graph,'b','g')
# DFS(graph,'b','g',{})
BidirectionalSearch(graph,'b','g')
