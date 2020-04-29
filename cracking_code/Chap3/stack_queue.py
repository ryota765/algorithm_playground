class Stack:
    def __init__(self):
        self.stack = []
        self.min = {}
        self.len = 0
    # データを先頭に追加
    def push(self,x):
        self.stack.append(x)
        self.len += 1
        if self.min == {} or self.min[self.len-1] > x:
            self.min[self.len] = x
        else:
            self.min[self.len] = self.min[self.len-1]
    # 先頭のデータを削除
    def pop(self):
        self.stack.pop()
        self.min[self.len] = self.min[self.len-1]
        del self.min[self.len]
        self.len -= 1
    # 先頭の要素を返す
    def peek(self):
        return self.stack[-1]
    # stackをprint
    def get_stack(self):
        print(self.stack)
    # 空かどうか確認
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def minimum(self):
        return self.min
    
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
        if len(self.queue) == 0:
            return True
        else:
            return False

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(2)
stack.push(5)
stack.push(1)
stack.get_stack()
print(stack.minimum())
stack.pop()
print(stack.minimum())