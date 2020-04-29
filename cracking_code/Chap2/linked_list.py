# Cellの定義
class Cell:
    def __init__(self,x,y=None):
        self.data = x
        self.next = y

    def first(self): return self.data
    def rest(self): return self.next

    def set_first(self,x): self.data = x
    def set_rest(self,x): self.next = x
    
# 連結リストの定義
class LinkedList:
    def __init__(self):
        self.top = None

    def print_list(self):
        cp = self.top
        print_list = []
        while cp:
            print_list.append(cp.first())
            cp = cp.rest()
        print(print_list)
    
    def insert(self,n,x):
        if n == 0 or not self.top:
            self.top = Cell(x, self.top)
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0: break
                cp = cp.rest()
            new_cp = Cell(x, cp.rest())
            cp.set_rest(new_cp)

    def delete(self,n):
        if n == 0:
            if self.top:
                self.top = self.top.rest()
                return True
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0:
                    cp.set_rest(cp.rest().rest())
                    return True
                cp = cp.rest()
        # whileループが終了(削除するindexがない) or n==0でtopがNoneの場合
        return False
        
    def index(self,x):
        n = 0
        cp = self.top
        while cp:
            if cp.first() == x: return n
            n += 1
            cp = cp.rest()
        return -1
    
    # 複数のindexを返す
    def indexes(self,x):
        n = 0
        cp = self.top
        idx_list = []
        while cp:
            if cp.first() == x: idx_list.append(n)
            n += 1
            cp = cp.rest()
        return idx_list

    # 重複している要素を削除 O(N)
    def delete_dup(self):
        dup_dict = {}
        cp = self.top
        cp_prev = None
        while cp:
            if cp.first() in dup_dict:
                cp_prev.set_rest(cp.rest())
            else:
                dup_dict[cp.first()] = True
            cp_prev = cp
            cp = cp.rest()
        return 'Success!'

    # 重複している要素を削除、バッファが使用できない場合 O(N^2)
    def delete_dup2(self):
        cp = self.top
        while cp:
            cp_prev = cp
            cp_sub = cp.rest()
            while cp_sub:
                if cp.first() == cp_sub.first():
                    cp_prev.set_rest(cp_sub.rest())
                cp_prev = cp_sub
                cp_sub = cp_sub.rest()
            cp = cp.rest()
        return 'Success!'

    # 後ろからk番目の要素を返す O(N)
    def kth_element_back(self,k):
        cp = self.top
        cp_k = self.top
        for i in range(k):
            cp_k = cp_k.rest()
        while cp_k.rest():
            cp = cp.rest()
            cp_k = cp_k.rest()
        return cp.first()
            
    # リストの分割 O(N)
    def divide(self,x):
        cp = self.top
        cp1 = None
        cp2 = None
        before_end = None
        while cp:
            if cp.first() >= x:
                if cp2 == None:
                    cp2 = Cell(cp.first(), None)
                else:
                    # cp2.set_rest(cp2)
                    # cp2.set_first(cp.first())
                    cp2 = Cell(cp.first(), cp2)
            else:
                if cp1 == None:
                    cp1 = Cell(cp.first(), None)
                    before_end = cp1
                else:
                    cp1 = Cell(cp.first(), cp1)
            cp = cp.rest()

        if before_end == None:
            self.top = cp2
        else:
            before_end.set_rest(cp2)
            self.top = cp1

    # リストで表された2数の和
    def place_sum(self,n):
        # リストの分割
        cp = self.top
        cp1 = None
        cp2 = None
        cp_return = None

        for i in range(n):
            if cp1 == None:
                cp1 = Cell(cp.first(), None)
            else:
                cp1 = Cell(cp.first(), cp1)
            cp = cp.rest()
        while cp:
            if cp2 == None:
                cp2 = Cell(cp.first(), None)
            else:
                cp2 = Cell(cp.first(), cp2)
            cp = cp.rest()
        
        # printで確認
        '''print_list1 = []
        while cp1:
            print_list1.append(cp1.first())
            cp1 = cp1.rest()
        print('cp1',print_list1)
        print_list2 = []
        while cp2:
            print_list2.append(cp2.first())
            cp2 = cp2.rest()
        print('cp2',print_list2)'''

        # 計算
        # count = 0
        n = 0
        # place = 0
        while cp1 != None and cp2 != None:
            # count += (cp1.first() + cp2.first() + n)//10 * 10**place
            print((cp1.first() + cp2.first() + n)%10)
            cp_return = Cell((cp1.first() + cp2.first() + n)%10, cp_return)
            n =  (cp1.first() + cp2.first() + n)//10
            # place += 1
            cp1 = cp1.rest()
            cp2 = cp2.rest()
        if cp1 != None:
            while cp1:
                # count += (cp1.first() + n)//10 * 10**place
                cp_return = Cell((cp1.first() + n)%10 , cp_return)
                n =  (cp1.first() + n)//10
                # place += 1
                cp1 = cp1.rest()
        elif cp2 != None:
            while cp2:
                # count += (cp2.first() + n)//10 * 10**place
                cp_return = Cell((cp2.first() + n)%10, cp_return)
                n =  (cp2.first() + n)//10
                # place += 1
                cp2 = cp2.rest()

        self.top = cp_return

        


l_list = LinkedList()
l_list.insert(0,1)
l_list.insert(0,2)
l_list.insert(0,4)
l_list.insert(0,2)
l_list.insert(0,3)
l_list.insert(0,1)
l_list.insert(0,2)
l_list.print_list()
l_list.place_sum(3)
l_list.print_list()


