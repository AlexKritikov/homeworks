if __name__ == '__main__':
# Task 1. A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".
    def favourite_movie (film):
        print(f'My favorite movie is named "{film}"')


# Task 2. Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.
    def make_country(name,capital):
        country_dict = dict()
        country_dict['name']=name
        country_dict['capital']=capital
        print(country_dict)


# Task 3. A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42
    def check(operator,*args):
        if operator=='+':
            print(sum(args))
        elif operator=='-':
            result_subtraction=args[0]
            for i in range(1,len(args)):
                result_subtraction-=args[i]
            print(result_subtraction)
        elif operator=='*':
            result_multiply = args[0]
            for i in range(1, len(args)):
                result_multiply *= args[i]
            print(result_multiply)
