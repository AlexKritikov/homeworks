from functools import wraps
if __name__ == '__main__':

# Task 1.Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example: "add called with 4, 5"
    def logger(func):
        def wrapper(*args):
            arguments=''
            for i in args:
                if args.index(i) < len(args)-1:
                    arguments+= str(i) + ', '
                else:
                    arguments+=str(i)
            print(f'{func.__name__} called with {arguments} ')
        return wrapper

# Task 2. Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
    def stop_words(word_list):
        def replace_words(function_t2):
            @wraps(function_t2)
            def wrapper(*args,**kwargs):
                f_2=function_t2(*args,**kwargs)
                new_list = []
                for i in f_2[:(len(f_2) - 1)].split():
                    if i in word_list:
                        i = '*'
                        new_list.append(i)
                    else:
                        new_list.append(i)
                new_list[-1] += '!'
                print(' '.join(new_list))
            return wrapper
        return replace_words
    @stop_words(['pepsi', 'BMW'])
    def create_slogan(name):
        return f"{name} drinks pepsi in his brand new BMW!"


# Task 3. Write a decorator "arg_rules" that validates arguments passed to the function.#
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result

    def arg_rules(type_: type, max_length: int, contains: list):
        def check_arguments (function_t3):
            @wraps(function_t3)
            def wrapper(*args):
                if all([isinstance(i,type_) for i in args]) == False:
                    raise TypeError('Pass only string please')
                elif all([len(i)<=max_length for i in args]) ==False:
                    raise ValueError('Too long argument, try something shorter')
                elif all([i in str(args) for i in contains]) == False:
                    raise ValueError('You should use certain symbols')
                else:
                    return function_t3(*args)
            return wrapper
        return check_arguments

    @arg_rules(type_=str, max_length=15, contains=['05', '@'])
    def create_slogan(name):
        return f"{name} drinks pepsi in his brand new BMW!"



