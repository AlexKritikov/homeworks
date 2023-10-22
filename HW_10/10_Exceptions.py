# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
# that calls oops inside a try/except statement to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?
if __name__ == '__main__':
    def oops():
        t1_tuple=(1,2,3,4,5)
        t1_variable=t1_tuple[5]

    def catch ():
        try:
            oops()
        except IndexError:
            print ('This tuple is not so long' )

# If we change oops to raise a KeyError we'll get a Key Error in catch function


# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).
    def algebra(a,b):
        return(a**2/b)
    try:
        algebra(a=int(input('Enter a number "a" please')), b=int(input('Enter a number "b" please')))
    except ValueError:
        print('Alarm!!! "a" and "b" should be only numbers')
    except ZeroDivisionError:
        print("You can't divide by zero")