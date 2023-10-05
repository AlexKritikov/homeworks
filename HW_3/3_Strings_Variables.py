if __name__ == '__main__':
    # Task 1. The greeting program. Make a program that has your name and the current  day of the week
    # stored as separate variables and then prints a message like this:
    # "Good day <name>! <day> is a perfect day to learn some python."
    # Note that < name > and < day > are predefined variables in source code.An additional bonus will be to use different
    # string formatting methods for constructing result string.

    import datetime

    day = datetime.date.today().strftime('%A')
    name = 'Alexander'
    print('Good day ' + name + '! ' + day + ' is a perfect day to learn some python.')
    print(f'Good day {name}! {day} is a perfect day to learn some python.')
    print('Good day {1}! {0} is a perfect day to learn some python.'.format(day, name))
    print('Good day %s! %s is a perfect day to learn some python.' % (name, day))

    # Task 2. Manipulate strings. Save your first and last name as separate variables, then use string
    # concatenation to add them together with a white space in between and print a greeting.
    first_name = 'Alexander'
    last_name = 'Kritikov'
    print('Hello, ' + first_name + ' ' + last_name + ', nice to meet you!')

    # Task 3. Using python as a calculator. Make a
    # program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
    # Addition
    # Subtraction
    # Division
    # Multiplication
    # Exponent(Power)
    # Modulus
    # Floor division
    numb_1=46
    numb_2=(-5)
    print(str(numb_1+numb_2) + ' is result of addition')
    print(str(numb_1-numb_2) + ' is result of subtraction')
    print(str(numb_1/numb_2) + ' is result of division')
    print(str(numb_1*numb_2) + ' is result of multiplication')
    print(str(numb_1**numb_2) + ' is result of exponent')
    print(str(numb_1 % numb_2) + ' is result of negative modulo')
    print(str(numb_1//numb_2) + ' is result of floor division')
