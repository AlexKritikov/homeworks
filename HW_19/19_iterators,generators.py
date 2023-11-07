if __name__ == '__main__':

    #Task 1. Create your own implementation of a built-in function enumerate, named 'with_index', which takes two
    # parameters: 'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function
    def with_index(iterable,start=0):
        if hasattr(iterable, '__iter__'):
            for i in iterable:
                yield start,i
                start+=1

    # Task 2.Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
    # 'start', 'end', and optional step. Tips: See the documentation for 'range' function
    def in_range(end,start=0,step=1):
        while start<end:
                yield start
                start+=step

    #  Task 3. Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
    # elements using square brackets syntax.

    class Own_implementation:#iteracia do elementa zadannogo znachenia
        def __init__(self,numbers,stop_number):
            self.numbers = numbers
            self.stop_number=stop_number
            self.index = -1

        def __iter__(self):
            return self
        def __next__(self):
            self.index += 1
            if self.numbers[self.index]<self.stop_number:
                return self.numbers[self.index]
            else:
                raise StopIteration

