if __name__ == '__main__':
    import datetime
# Task 1. School
# Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
# should only be available to the teacher.
    class Person():
        def __init__(self,name,surname,sex, age,nationality,religion):
            self.name=name
            self.surname=surname
            self.sex=sex
            self.age=age
            self.nationality=nationality
            self.religion=religion
        def eat(self):
            return 'I can eat'
        def drink(self):
            return 'I can drink'
    class Teacher(Person):
        def __init__(self,name,surname,sex, age,nationality,religion,grade:int,salary,vacation:int):
            super().__init__(name,surname,sex, age,nationality,religion)
            self.grade=grade
            self.salary=salary
            self.vacation=vacation
        def teach(self):
            return( 'I can teach')

    class Student(Person):
        def __init__(self,name,surname,sex, age,nationality,religion,average_mark,course,speciality):
            super().__init__(name,surname,sex, age,nationality,religion)
            self.marks=average_mark
            self.course=course
            self.speciality=speciality
        def study(self):
            return( 'I can study')

#Task 2. Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
    class Mathematician():
        def square_nums(self,nums:list):
            return ([i**2 for i in nums])
        def remove_positives(self,nums:list):
            return list(filter(lambda num: num < 0, nums))
        def filter_leaps(self,nums:list):
            return list(filter(lambda num: (num % 4==0 and num % 100 != 0) or num %400==0 , nums))


#Task 3. Product Store. Write a class Product that has three attributes:
# # type
# # name
# price
#
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
# classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
    # add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
    # store(30 percent)

    # set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
    # identifiers (type or name). The discount must be specified in percentage

    # sell_product(product_name, amount) - removes a particular amount of products from the store if available,
    #  in other case raises an error. It also increments income if the sell_product method succeeds.

    # get_income() - returns amount of many earned by ProductStore instance.

    # get_all_products() - returns information about all available products in the store.

    # get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
    class Product():
        def __init__(self,type,name,price):
            self.type=type
            self.name=name
            self.price=price
    class ProductStore():
        warehouse=[]
        income=0
        def add(self, product, amount):
            self.product = product
            self.amount = amount
            if len(self.warehouse)==0:
                self.warehouse_product = dict()
                self.warehouse_product['name']=product.name
                self.warehouse_product['type'] =product.type
                self.warehouse_product['discont'] = 0
                self.warehouse_product['amount'] = amount
                self.warehouse_product['price'] = round(product.price*1.3,2)
                self.warehouse.append(self.warehouse_product)
            else:
                self.counter_product=0
                for i in self.warehouse:
                    if product.name == i['name'] and product.type == i['type'] :
                        i['amount']+= amount
                        i['price']=round(1.3*product.price*((100-i['discont'])/100),2)
                        self.counter_product+=1
                if self.counter_product==0:
                    self.warehouse_product = dict()
                    self.warehouse_product['name'] = product.name
                    self.warehouse_product['type'] = product.type
                    self.warehouse_product['discont'] = 0
                    self.warehouse_product['amount'] = amount
                    self.warehouse_product['price'] = round(product.price*1.3,2)
                    self.warehouse.append(self.warehouse_product)

        def set_discount(self,identifier:str, percent:int, identifier_type='name'):
            self.id=identifier
            self.discont=percent
            self.counter_product = 0
            for i in self.warehouse:
                if i[identifier_type] ==self.id:
                    i['discont']=self.discont
                    i['price']=round(i['price']*((100-i['discont'])/100),2)
                    self.counter_product += 1
            if self.counter_product == 0:
                raise ValueError("We don't have such product or type of products")

        def sell_product(self,product_name, amount):
            self.product_name=product_name
            self.amount=amount
            self.counter_product = 0
            for i in self.warehouse:
                if product_name == i['name']:
                    if i['amount'] < self.amount:
                        raise ValueError(f"We don't have so many/much {i['name']},we have only {i['amount']}")
                    else:
                        i['amount'] -= self.amount
                        self.counter_product += 1
                        self.income+=self.amount * i['price']
            if self.counter_product == 0:
                raise ValueError("We don't have such product")

        def get_income(self):
            return self.income

        def get_all_products(self):
            return list(filter(lambda i: i['amount'] > 0, self.warehouse))

        def get_product_info(self,product_name):
            self.product_name=product_name
            self.counter_product = 0
            for i in self.warehouse:
                if self.product_name == i['name']:
                    self.info_list=[]
                    self.info_list.append(i['name'])
                    self.info_list.append(i['amount'])
                    self.counter_product += 1
                    return tuple(self.info_list)
            if self.counter_product == 0:
                raise ValueError("We don't have such product")


# Task 4. Custom exception
# Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its
# functionality to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality
# for saving messages to file
    import logging
    from logging import FileHandler
    from datetime import datetime
    class CustomException(Exception):
        def __init__(self, msg):
            self.msg=msg

            self.logger = logging.getLogger('File_logger')
            self.logger.addHandler(FileHandler('logs.txt'))
            self.logger.setLevel(logging.DEBUG)

            self.log_message = str(datetime.now().date()) + ' ' + str(datetime.now().time()) + ' ' + self.msg
            self.logger.info(self.log_message)


