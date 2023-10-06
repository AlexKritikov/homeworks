if __name__ == '__main__':

# Task 1. String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'#
#  Expected Result : 'held'
# Sample String: 'my'#
# Expected Result : 'mymy'
# Sample String: 'x'
# Expected Result: Empty String.
#
# Tips:#
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters>>>>>>>
    new_string=input('Enter a new string please')
    if len(new_string)<2:
        print('String is too short, enter another one')
    else:
        print(new_string[:2] + new_string[-2:])

# # Task 2. The valid phone number program.
# # Make a program that checks if a string is in the right format for a phone number.
# # The program should check that the string contains only numerical characters and is only 10 characters long.
# # Print a suitable message depending on the outcome of the string evaluation.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    while True:
        phone=input('Enter your phone number')
        if phone == 'No':
            break
        elif len(phone)!= 10:
            print('Phone number is not correct. It should contain 10 characters')
        elif phone.isdigit() == False:
            print('Phone number should contain only numerical characters')
        else:
            print("Thank you ! System receive your phone number")
            break



# Task 3. The math quiz program.
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    answer = 2 + 3 * 4 - 3 ** 2 / 4
    while True:
        num_question = input('Answer the quiz 2+3*4-3**2/4= ?')
        if num_question == ('No'):
            break
        elif num_question != str(answer):
            print('You are wrong. Try again')
        else:
            print("Congratulations ! You are wright")
            break

# Task 4. The name check.
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.

    while True:
        name_stored = 'Alexander'
        name_request = input('Please enter your name')
        if name_request == ('No'):
            break
        elif name_stored.capitalize() != name_request.capitalize():
            print('You are wrong. Try again')
        else:
            print("Congratulations ! You are wright")
            break
