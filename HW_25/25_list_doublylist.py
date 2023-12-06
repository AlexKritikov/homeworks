if __name__ == '__main__':

# Task 1.Extend UnsortedList
# Implement append, index, pop, insert methods for UnsortedList. Also implement a slice method, which will take two
# parameters 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including
# the stop position.
    class Node:
        def __init__(self,data=None,next=None):
            self.data=data
            self.next=next
        #Get methods
        def get_data(self):
            return self.data
        def get_next(self):
            return self.next
        # Set methods
        def set_data(self,data):
            self.data=data
        def set_next(self,next):
            self.next=next

    class UnsortedList:
        def __init__(self):
            self.head=None

        def append (self,data):
            new_node=Node(data)
            current_node=self.head
            if current_node==None:
                self.head=new_node
                return

            while current_node.get_next()!=None:
                current_node=current_node.get_next()
            current_node.set_next(new_node)
            return
        def size(self):
            current_node = self.head
            size_list=0
            while current_node != None:
                current_node = current_node.get_next()
                size_list+=1
            return size_list


        def index(self,index):
            if index<0 or index>=self.size():
                raise IndexError('This index is out of range in unsorted list')
            current_node=self.head
            i=0
            while current_node and i!=index:
                current_node = current_node.get_next()
                i+=1
            return current_node


        def pop(self,index=None):
            if index!=None:
                if index<0 or index>=self.size():
                    raise IndexError('This index is out of range in unsorted list')
                else:
                    i=0
                    current_node=self.head
                    if index==0:
                        self.head=current_node.get_next()
                        return current_node

                    else:
                        current_node = self.head
                        while i!=index-1:
                            current_node = current_node.get_next()
                            i += 1
                        pop_element=current_node.get_next()
                        current_node.set_next(current_node.get_next().get_next())
                        return pop_element
            else:
                current_node = self.head
                while current_node.get_next().get_next()!=None:
                    current_node = current_node.get_next()
                pop_element = current_node.get_next()
                current_node.set_next(current_node.get_next().get_next())
                return pop_element

        def insert(self,data,index:int ):
            if index < 0 or index >= self.size():
                raise IndexError('This index is out of range in unsorted list')
            else:
                i = 0
                new_node=Node(data)
                current_node = self.head
                if index == 0:
                    new_node.set_next(current_node)
                    self.head = new_node
                    return

                else:
                    current_node = self.head
                    while i != index - 1:
                        current_node = current_node.get_next()
                        i += 1
                    new_node.set_next(current_node.get_next())
                    current_node.set_next(new_node)
                    return
        def slice(self,start: int, stop: int):
            if stop < 0 or stop > self.size():
                raise IndexError('This index is out of range in unsorted list')
            elif start > stop:
                raise ValueError('Start should be less or equal to stop')
            else:
                current_node = self.head
                i=0
                while i!=start:
                    current_node=current_node.get_next()
                    i+=1
                self.head=current_node
                while i != stop-1:
                    current_node = current_node.get_next()
                    i += 1
                current_node.set_next(None)
                return
        def show(self):
            current_node=self.head
            output=''
            while current_node!=None:
                    output+=str(current_node.get_data())+' -> '
                    current_node=current_node.get_next()
            print(output)

# Task 2. Implement a stack using a singly linked list.
    class Stack(UnsortedList):
        def stack_in(self,data):
            self.append(data)
        def stack_out(self):
            self.pop()

# Task 3. Implement a queue using a singly linked list.
    class Queue(UnsortedList):
        def queue_in(self, data):
            self.append(data)
        def queue_out(self):
            self.pop(0)