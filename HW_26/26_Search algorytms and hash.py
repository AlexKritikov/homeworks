if __name__ == '__main__':
    # Task1.Binary search.Recursion
    def binary_search_recursion(array,item,first_position,last_position):
        if last_position < first_position:
            print('We dont have this item in sequence')
            return False
        center = (last_position + first_position) // 2
        if array[center] > item:
            return binary_search_recursion(array,item,first_position,center-1)
        elif array[center]<item:
            return binary_search_recursion(array, item, center + 1, last_position)
        else:
            return center

    # sequence=['a','b','c','d','e','f','g','h']
    # print(binary_search_recursion(sequence,'d',0,len(sequence)-1))

    #Task2. Fibonacci search
    class Fibonacci_search():#O(logN)
        def init(self,seq,element):
            self.seq=seq
            self.element=element
            self.N=len(seq)
            self.found_element=False
            self.flag=False

        def fibonacci(self,n):
            fib_list = [0, 1]
            fib_num = 0
            if n <2:
                return fib_num
            else:
                for i in range(2, n + 1):
                    fib_num = fib_list[-1] + fib_list[-2]
                    fib_list.append(fib_num)
                return fib_num

        def k_number(self):
            i=0
            while self.fibonacci(i)<self.N+1:
                i+=1
            return i-1

        def search(self):
            self.k=self.k_number()
            self.M=self.fibonacci(self.k+1)-(self.N+1)
            self.index=self.fibonacci(self.k)-self.M
            self.p=self.fibonacci(self.k-1)
            self.q=self.fibonacci(self.k-2)
            self.check_index()
            if self.flag==False:
                return self.index
            else:
                return f'We dont have such element=({self.element}) in our sequence'
        def go_left(self):
            if self.q==0:
                self.flag=True
                self.found_element = True

            else:
                self.index=self.index-self.q
                (self.p,self.q)=(self.q,self.p-self.q)
        def go_right(self):
            if self.p==1:
                self.flag = True
                self.found_element = True
            else:
                self.index=self.index+self.q
                self.p=self.p-self.q
                self.q=self.q-self.p

        def check_index(self):
            while self.found_element==False:
                if self.index<0:
                    self.go_right()
                elif self.index>=self.N:
                    self.go_left()
                else:
                    if self.element < self.seq[self.index]:
                        self.go_left()
                    elif self.element > self.seq[self.index]:
                        self.go_right()
                    else:
                        print(f'Element {self.element} is found')
                        self.found_element=True
    # seq = [-2, 0, 3, 5, 7, 9, 11, 15, 18, 21]
    # s=Fibonacci_search()
    # s.init(seq,21)
    # print(s.search())

    #Task3. Implement in (__contains__) and len (__len__) methods for HashTable
    class Hashtable:#For dict
        def __init__(self):
            self.table=dict()
            self.length=0
        def add(self,key,value):
            self.key=key
            self.value=value
            self.table[self.key]=self.value
        def __str__(self):
            return f'{self.table}'
        def __repr__(self):
            return self.__str__()

        def in_ (self,item):
            for key in self.table:
                if item==key:
                    return True
            return False
        def len_(self):
            for key in self.table:
                self.length+=1
            return self.length

    # table_draft=Hashtable()
    # table_draft.add('a',1)
    # table_draft.add('b',2)
    # table_draft.add('c',3)
    # print(table_draft.in_('b'))
    # print(table_draft.in_('c'))
    # print(table_draft.in_('u'))
    # print(table_draft.len_())

    class Hashtable_set():  # For set of integers
        def __init__(self):
            self.size=10
            self.set_group=[[] for i in range(0,self.size)]
            self.length=0
        def __str__(self):
            return f'{self.set_group}'

        def __repr__(self):
            return self.__str__()

        def add(self,x:int):
            if not self.in_(x):
                self.set_group[x%self.size].append(x)
                print(f'We add new element={x}')
                self.length+=1
            else:
                print(f'Weve already add this element={x}')
                return False
        def in_(self,x:int):
            for i in self.set_group[x%self.size]:
                if i ==x:
                        print(f'Weve found this element={x} in bucket number {x%self.size}')
                        return x%self.size
            print('We dont have such element')
            return False
        def len_(self):
            return self.length
        def delete(self, x:int):
            bucket=x % self.size
            target_bucket=self.set_group[bucket]
            for i in range(0,len(target_bucket)):
                if target_bucket[i] == x:
                    print(f'Weve deleted element={x}')
                    target_bucket.pop(i)
                    self.length-=1

    # set_of_int=Hashtable_set()
    # set_of_int.add(3)
    # set_of_int.add(5)
    # set_of_int.add(5)
    # set_of_int.add(5)
    # set_of_int.add(-3)
    # set_of_int.add(4)
    # set_of_int.add(9)
    # set_of_int.add(10)
    # set_of_int.add(9)
    # print(set_of_int.delete(5))
    # print(set_of_int)
    # print(set_of_int.in_(-9))
    # print(set_of_int.in_(-3))
    # print(set_of_int.in_(5))
    # print(set_of_int.len_())



