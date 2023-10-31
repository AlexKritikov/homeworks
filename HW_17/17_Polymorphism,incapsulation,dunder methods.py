if __name__ == '__main__':
    import math
# Task 1.Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their
# own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be
# to print ‘meow’.Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and
# performs talk method on input parameter.
    class Animal:
        def __init__(self, name):
            self.name = name
    class Cat(Animal):
        def talk(self):
            return 'Meow!'
    class Dog(Animal):
        def talk(self):
            return 'Woof!'

    def simple_func(animal:Animal):
        return (animal.talk())

# Task 2. Library
# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
#
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
# list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
    class Author:
        books = []
        def __init__(self,name, country, birthday):
            self.name = name
            self.country = country
            self.birthday = birthday
        def __repr__(self):
            return self.name
        def __str__(self):
            return f'The author is {self.name} from {self.country}'
    class Library:
        books=[]
        authors=[]
        def __init__(self,name):
            self.name=name
        def __repr__(self):
            return self.__str__()
        def __str__(self):
            return f'The biggest library of our city is "{self.name}"'
        def  new_book(self,name: str, year: int, author: Author):
            self.name = name
            self.year = year
            self.author = author

            self.library_book = dict()
            self.library_book['name'] = self.name
            self.library_book['year'] = self.year
            self.library_book['author'] = self.author.name
            self.books.append(self.library_book)

            if len(Author.books)==0:
                Author.books.append(self.library_book)
                Book.books_exist+=1
            else:
                self.counter_books=0
                for i in Author.books:
                    if self.name == i['name'] and self.author.name == i['author'] :
                        self.counter_books+=1
                if self.counter_books==0:
                    Author.books.append(self.library_book)
                    Book.books_exist += 1

            if len(self.authors) == 0:
                self.authors.append(self.author)
            else:
                self.counter = 0
                for i in self.authors:
                    if self.author.name == i.name and self.author.birthday == i.birthday and self.author.country == i.country:
                        self.counter+= 1
                if self.counter == 0:
                    self.authors.append(self.author)

            return Book(self.name,self.year,self.author)

        def group_by_author(self,author: Author):
            self.author = author
            self.counter_author = 0
            for i in self.authors:
                if self.author.name == i:
                    self.counter_author+=1
            if self.counter_author==0:
                return "We don't have such author in our library"
            else:
                return [i['name'] for i in self.books if i['author']==self.author.name]

        def group_by_year(self,year: int):
            self.year = year
            if len([i['name'] for i in self.books if i['year'] == self.year])==0:
                return "We don't have such books in our library"
            else:
                return [i['name'] for i in self.books if i['year'] == self.year]

    class Book(Author):
        books_exist=0
        def __init__(self,name:str, year:int, author:Author):
            self.name = name
            self.year=year
            self.author = author

        def __repr__(self):
            return self.name
        def __str__(self):
            return f' The book name is "{self.name}"'


# Task 3. Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
# перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між
# об'єктами класу Fraction

    class Fraction:
        def __init__(self,a:int,b:int):
            self.a=a
            self.b=b
        def __add__(self, other):
            if not isinstance(other,type(self)):
                raise ValueError('wrong type for operand')
            elif self.b==0 or other.b==0:
                raise ZeroDivisionError('Denominator cant be "0"')
            else:
                self.k=(self.b*other.b)/math.gcd(self.b,other.b)
                return Fraction(int(self.k/self.b*self.a+self.k/other.b*other.a), int(self.k))

        def __sub__(self, other):
            if not isinstance(other, type(self)):
                raise ValueError('wrong type for operand')
            elif self.b == 0 or other.b == 0:
                raise ZeroDivisionError('Denominator cant be "0"')
            else:
                self.k = (self.b * other.b) / math.gcd(self.b, other.b)
                return Fraction(int(self.k / self.b * self.a - self.k / other.b * other.a), int(self.k))
        def __mul__(self, other):
            if not isinstance(other,type(self)):
                raise ValueError('wrong type for operand')
            elif self.b==0 or other.b==0:
                raise ZeroDivisionError('Denominator cant be "0"')
            else:
                return Fraction(self.a*other.a, self.b*other.b)

        def __truediv__(self, other):
            if not isinstance(other, type(self)):
                raise ValueError('wrong type for operand')
            elif self.b == 0 or other.b == 0:
                raise ZeroDivisionError('Denominator cant be "0"')
            elif other.a==0:
                raise ZeroDivisionError('You cant divide by zero')
            else:
                return Fraction(self.a * other.b, self.b * other.a)
        def __str__(self):
            return f'The result is Fraction({self.a},{self.b})'
        def __repr__(self):
            return self.__str__()