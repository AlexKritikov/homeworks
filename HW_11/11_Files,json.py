# Task 1. Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then
# write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system
# command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
#
# Note: file write methods do not add newline characters to your strings; add an explicit "\n" at the end of the string
# if you want to fully terminate the line in the file.
import json

if __name__ == '__main__':

    def create_file():
        with open('myfile.txt','w') as new_file:
            new_file.write('Hello file world')
    def print_file():
        with open('myfile.txt','r')  as content:
            print(content.read())
# We can see a new file in the directory where we create and run our scripts
# If we open file for writing and enter a different directory pass we'll create a new file in this directory


# Task 2.Extend Phonebook application
# Functionality of Phonebook application:
#
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
##
# The first argument to the application should be the name of the phonebook. Application should load JSON data,
# if it is present in the folder with application, else raise an error. After the user exits, all data should be saved
# to loaded JSON.

    import os
    def search_first_name(**kwargs):#1
        user_first_name = input('Enter searching first name please')
        for i in phonebook_dict['items']:
            if i['first_name'] == user_first_name:
            print(i)
    def search_last_name(**kwargs):#2
        user_last_name = input('Enter searching last name please')
        for i in phonebook_dict['items']:
            if i['last_name'] == user_last_name:
            print(i)

    def search_full_name(**kwargs):#3
        user_full_name = input('Enter searching full name please')
        for i in phonebook_dict['items']:
            if i['full_name'] == ' '.join(user_full_name.split()):
            print(i)

    def search_telephone_number(**kwargs):#4
        user_telephone_number = input('Enter searching telephone number please')
        for i in phonebook_dict['items']:
            if i['telephone_number'] == user_telephone_number:
            print(i)

    def search_city(**kwargs):#5
        user_city = input('Enter searching city please')
        for i in phonebook_dict['items']:
            if i['city'] == user_city:
            print(i)


    def delete_telephone_number(**kwargs):#6
        user_telephone_number = input('Enter telephone number you want to delete please')
        for i in phonebook_dict['items']:
            if i['telephone_number'] == user_telephone_number:
                phonebook_dict['items'].remove(i)

    def add_entry(**kwargs):#7
        user_first_name = input('Enter first name you want to add')
        user_last_name = input('Enter last name you want to add')
        user_full_name = input('Enter full name you want to add')
        user_telephone_number = input('Enter telephone number you want to add')
        user_city = input('Enter city you want to add')
        phonebook_dict['items'].append(dict())
        phonebook_dict['items'][len(phonebook_dict['items'])-1]['first_name']= user_first_name
        phonebook_dict['items'][len(phonebook_dict['items']) - 1]['last_name'] = user_last_name
        phonebook_dict['items'][len(phonebook_dict['items']) - 1]['full_name'] = user_full_name
        phonebook_dict['items'][len(phonebook_dict['items']) - 1]['telephone_number'] = user_telephone_number
        phonebook_dict['items'][len(phonebook_dict['items']) - 1]['city'] = user_city


    def update_record(**kwargs):#8
        user_telephone_number = input('Enter telephone number you want to update please')
        for i in phonebook_dict['items']:
            if i['telephone_number'] == user_telephone_number:
                while True:
                    update_choice = input('If you want to update first name - enter "1", last name - "2", '
                                          'full name - "3", telephone number - "4", city - "5", exit - "0"')
                    if update_choice == '0':
                        break
                    elif update_choice == '1':
                        user_first_name = input('Enter information you want to update in first name')
                        i['first_name'] = user_first_name
                        continue
                    elif update_choice == '2':
                        user_last_name = input('Enter information you want to update in last name')
                        i['last_name'] = user_last_name
                        continue
                    elif update_choice == '3':
                        user_full_name = input('Enter information you want to update in full name')
                        i['full_name'] = user_full_name
                        continue
                    elif update_choice == '4':
                        user_telephone_number = input('Enter information you want to update in telephone number')
                        i['telephone_number'] = user_telephone_number
                        continue
                    elif update_choice == '5':
                        user_city = input('Enter information you want to update in city')
                        i['city'] = user_city
                        continue

user_application = input('Please enter the name of the .json data')
if (f'{user_application}.json' in os.listdir(os.getcwd())) == False:
    raise FileNotFoundError("We don't have such JSON data")
else:
    phonebook_dict = json.load(open('Phonebook.json'))
    while True:
        user_functional = input('If you want to search by first name - enter "1", last name - "2", '
                              'full name - "3", telephone number - "4", city - "5", delete record by telephone '
                                'number - "6", add entry - "7", update record - 8,  exit - "0"')
        if user_functional == '0':
            break
        elif user_functional == '1':
            search_first_name()
            continue
        elif user_functional == '2':
            search_last_name()
            continue
        elif user_functional == '3':
            search_full_name()
            continue
        elif user_functional == '4':
            search_telephone_number()
            continue
        elif user_functional == '5':
            search_city()
            continue
        elif user_functional == '6':
            delete_telephone_number()
            continue
        elif user_functional == '7':
            add_entry()
            continue
        elif user_functional == '8':
            update_record()
            continue
    with open('Phonebook.json', 'w') as phonebook:
        json.dump(phonebook_dict, phonebook)





