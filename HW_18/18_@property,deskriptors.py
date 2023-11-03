if __name__ == '__main__':
    # """Task 1. Create a class method named `validate`, which should be called from the `__init__` method to validate
    # parameter email, passed to the constructor. The logic inside the `validate` method could be to check if the passed
    # email parameter is a valid email string.

    class EmailValidation:
        def __init__(self,x):
            if self.validate(x):
                self.x=x
                print (f'Ok. Email "{self.x}" is valid')

        def validate(cls,email):
            if email.count('@') == 1:
                prefix = email.split('@')[0]
                if all('a' <= i <= 'z' or i == '.' or i == '_' or i == '-' or i == ' ' or i.isdigit() for i in prefix):
                    if prefix[0] == '.' or prefix[-1] == '.':
                        raise ValueError("Dot is not allowed to be the first or last character")
                    else:
                        for i in range(0, len(prefix) - 1):
                            if prefix[i] == '.' and prefix[i + 1] == prefix[i]:
                                raise ValueError("Dot shouldn't appear consecutively")
                else:
                    raise ValueError(
                        'Email prefix may contain only letters (a-z), numbers, underscores, periods, and dashes')
                domain = email.split('@')[1]
                if all('a' <= i <= 'z' or i == '.' or i == '-' for i in domain):
                    if domain.count('.')>0 and all('a' <= i <= 'z' for i in domain[domain.rindex('.') + 1:len(domain)]) and (len(domain) - 1) - (domain.rindex('.')) >= 2:
                        pass
                    else:
                        raise ValueError('Email domain should end by dot and 2 characters at least')
                else:
                    raise ValueError('Email domain may contain only letters (a-z),dots and dashes')
            else:
                raise ValueError('Email adress should contain "@')
            return True

    # """Task 2. Implement 2 classes, the first one is the Boss and the second one is the Worker.
    # Worker has a property 'boss', and its value must be an instance of Boss.
    # You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
    # workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
    # of Boss class to workers list directly via access to attribute, use getters and setters instead!
    # You can refactor the existing code.
    # id_ - is just a random unique integer
    class Boss:
        def __init__(self,name: str, company: str):
            self.name = name
            self.company = company
            self.workers = []
    class Worker:
        def __init__(self,name: str, company: str, boss: Boss):
            self.name = name
            self.company = company
            self.boss = boss

        @property
        def get_a_job(self):
            if self.boss is None:
                return (f"My name is {self.name}. I'm unemployed")
            else:
                return(f'My name is {self.name}.My boss is {self.boss}.I work for {self.company}')

        @get_a_job.setter
        def get_a_job(self,boss):
            if isinstance(boss,Boss):
                self.boss_list=boss.workers
                self.boss=boss.name
                self.company=boss.company
                print(f'{self.name} has got a job in new company')
                if self.name not in self.boss_list:
                    self.boss_list.append(self.name)
                    return(f'{boss.name} get a new employee. His/her name is {self.name}')

            else:
                return (f'Sorry, but {self.name} look for a job in another company')
        @get_a_job.deleter
        def get_a_job(self):
            print (f"I've resigned from {self.company}")
            if self.name in self.boss_list:
                self.boss_list.remove(self.name)
                self.boss=None
                self.company=None
            else:
                return ('We dont have such employee')

    # Task 3. Write a class TypeDecorators which has several methods for converting results of functions to a specified
    # type (if it's possible):
    # methods:
    # to_int
    # to_str
    # to_bool
    # to_float
    #
    ## Don't forget to use @wraps
    from functools import wraps
    class TypeDecorators:
        def to_int(func):
            @wraps(func)
            def wrapper(*args):
                for i in args:
                    if isinstance(i, float) or isinstance(i, bool) or (isinstance(i, str) and i.isnumeric()) or isinstance(
                        i, int):
                        return (int(i))
                    else:
                        raise ValueError('We cant convert this type')
            return wrapper

        def to_str(func):
            @wraps(func)
            def wrapper(*args):
                for i in args:
                    if isinstance(i, float) or isinstance(i, bool) or isinstance(i, str) or isinstance(i, int):
                        return(str(i))
                    else:
                        raise ValueError('We cant convert this type')
            return wrapper

        def to_bool(func):
            @wraps(func)
            def wrapper(*args):
                for i in args:
                    if isinstance(i, bool) or isinstance(i, int) or isinstance(i, str) or isinstance(i, float):
                        return (bool(i))
                    else:
                        raise ValueError('We cant convert this type')
            return wrapper

        def to_float(func):
            @wraps(func)
            def wrapper(*args):
                for arg in args:
                    if isinstance(arg, bool) or isinstance(arg, int) or (
                            isinstance(arg, str) and all(i.isdigit() or i == '.' for i in arg)) or isinstance(arg, float):
                        return (float(arg))
                    else:
                        raise ValueError('We cant convert this type')
            return wrapper


