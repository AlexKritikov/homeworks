if __name__ == '__main__':

    # Task 1
    # Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of
    # Stack.
    def t1_program(sequence_t1):
        symbols=[]
        for i in sequence_t1:
            symbols.append(i)
        while len(symbols)>0:
            print(symbols.pop())

    # Task 2
    # Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly
    # brackets are "balanced."
    def t2_program(sequence_t2):
        left_symbols='([{'
        right_symbols=')]}'
        left_side=[]
        right_side=[]

        for i in sequence_t2:
                if i in left_symbols and len(left_side) == len(right_side):
                    left_side.append(i)
                elif i in left_symbols and (len(left_side) - len(right_side)) >= 1:
                    left_side.insert(len(right_side) - len(left_side), i)
                elif i in right_symbols and len(left_side) == len(right_side):
                    print('You couldnt start with right-side brackets')
                    right_side.append(i)
                    break
                elif i in right_symbols and (len(left_side) - len(right_side)) >= 1:
                    right_side.append(i)

        if len(left_side) != len(right_side):
            print('Brackets are not balanced')
        else:
            print('Sides completed')
            counter=0
            for i in range(len(left_side)):
                if ((left_side[i] == '(' and right_side.pop() != ')') or (
                        left_side[i] == '[' and right_side.pop() != ']') or (
                        left_side[i] == '{' and right_side.pop() != '}')):
                    print('You should use proper type of brackets')
                    break
                else:
                    counter+=1
            if counter==len(left_side):
                print('Good. Brackets are balanced')

    # Task 3
    # Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. Any
    # other element must remain on the stack respecting their order. Consider the case in which the element is not found -
    # raise ValueError with proper info Message
    #
    # Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue. Any
    # other element must remain in the queue respecting their order. Consider the case in which the element is not found -
    # raise ValueError with proper info Message

    class Stack:
        def __init__(self,items):
            self._items = items

        def is_empty(self):
            return bool(self._items)

        def push(self, item):
            self._items.append(item)

        def pop(self):
            return self._items.pop()

        def peek(self):
            return self._items[len(self._items) - 1]

        def size(self):
            return len(self._items)

        def __repr__(self):
            representation = "<Stack>\n"
            for ind, item in enumerate(reversed(self._items), 1):
                representation += f"{ind}: {str(item)}\n"
            return representation

        def __str__(self):
            return self.__repr__()

        def get_from_stack(self,e) -> bool:
            for i in self._items:
                if i==e:
                    return e
            raise ValueError (f'Element "{e}" is not in Stack')


    class Queue:
        def __init__(self,items):
            self._items = items

        def is_empty(self):
            return bool(self._items)

        def enqueue(self, item):
            self._items.insert(0, item)

        def dequeue(self):
            return self._items.pop()

        def size(self):
            return len(self._items)

        def __repr__(self):
            representation = "<Queue>\n"
            for ind, item in enumerate(reversed(self._items), 1): # 1 - exit first, 2- exit second
                representation += f"{ind}: {str(item)}\n"
            return representation

        def __str__(self):
            return self.__repr__()

        def get_from_queue(self,e):
            for i in self._items:
                if i == e:
                    return e
            raise ValueError(f'Element "{e}" is not in Queue')