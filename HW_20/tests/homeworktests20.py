from unittest import TestCase, main
import json
import os

# Task_1.Pick your solution to one of the exercises in this module. Design tests for this solution and write tests
# using unittest library.

# Exercise.
#  Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside the
#  list are positive, execute the first function on that list and return the result of it. Otherwise, return the result
#  of the second one
nums = [1, 2, 8, 4, 10]


def square_nums():
    return [num ** 2 for num in nums]


def remove_negatives():
    return list(filter(lambda num: num >= 0, nums))


def choose_func():
    count = 0
    if sum([count + 1 for i in nums if i < 0]) > 0:
        return remove_negatives()
    else:
        return square_nums()


class TaskTest1(TestCase):

    def test_type(self):  # function returns list
        self.assertTrue(type(choose_func()) == list)

    def test_positive_elements(self):  # function returns only positive elements in list
        self.assertTrue(all(i >= 0 for i in choose_func()))

    def test_square_elements(self):  # function returns squared elements
        self.assertTrue(all(i >= 0 for i in nums))
        self.assertTrue(all(choose_func()[i] == nums[i] ** 2 for i in range(len(nums))))


# # Task_2. Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this
# # solution and write tests using unittest library


user_application = ('Phonebook')
if (f'{user_application}.json' in os.listdir(os.getcwd())) == False:
    raise FileNotFoundError("We don't have such JSON data")
else:
    phonebook_dict = json.load(open(f'{user_application}.json'))


def search_first_name(**kwargs):  # 1
    user_first_name = 'Anton'
    for i in phonebook_dict['items']:
        if i['first_name'] == user_first_name:
            return (i)


def search_last_name(**kwargs):  # 2
    user_last_name = 'Shalamov'
    for i in phonebook_dict['items']:
        if i['last_name'] == user_last_name:
            return (i)


def search_full_name(**kwargs):  # 3
    user_full_name = 'Anton Sergijovich Shalamov'
    for i in phonebook_dict['items']:
        if i['full_name'] == ' '.join(user_full_name.split()):
            return (i)


def search_telephone_number(**kwargs):  # 4
    user_telephone_number = '0963051160'
    for i in phonebook_dict['items']:
        if i['telephone_number'] == user_telephone_number:
            return (i)


def search_city(**kwargs):  # 5
    user_city = 'Rostov-on-Don'
    for i in phonebook_dict['items']:
        if i['city'] == user_city:
            return (i)


def delete_telephone_number(**kwargs):  # 6
    user_telephone_number = '0673154370'
    for i in phonebook_dict['items']:
        if i['telephone_number'] == user_telephone_number:
            phonebook_dict['items'].remove(i)
            return i


def add_entry(**kwargs):  # 7
    user_first_name = 'Tetyana'
    user_last_name = 'Baranovskaja'
    user_full_name = 'Tetyana Petrovna Baranovskaja'
    user_telephone_number = '0974514910'
    user_city = 'Tel-a-viv'
    phonebook_dict['items'].append(dict())
    phonebook_dict['items'][len(phonebook_dict['items']) - 1]['first_name'] = user_first_name
    phonebook_dict['items'][len(phonebook_dict['items']) - 1]['last_name'] = user_last_name
    phonebook_dict['items'][len(phonebook_dict['items']) - 1]['full_name'] = user_full_name
    phonebook_dict['items'][len(phonebook_dict['items']) - 1]['telephone_number'] = user_telephone_number
    phonebook_dict['items'][len(phonebook_dict['items']) - 1]['city'] = user_city
    return phonebook_dict['items'][len(phonebook_dict['items']) - 1]


def update_record(**kwargs):  # 8
    user_telephone_number = '0959119354'
    for i in phonebook_dict['items']:
        if i['telephone_number'] == user_telephone_number:
            update_choice = "5"

            if update_choice == '0':
                return None

            elif update_choice == '1':
                user_first_name = 'Valentin'
                i['first_name'] = user_first_name
                return i

            elif update_choice == '2':
                user_last_name = 'Karkavin'
                i['last_name'] = user_last_name
                return i

            elif update_choice == '3':
                user_full_name = 'Valentin Sergijovich Karkavin'
                i['full_name'] = user_full_name
                return i

            elif update_choice == '4':
                user_telephone_number = '0677093147'
                i['telephone_number'] = user_telephone_number
                return i

            elif update_choice == '5':
                user_city = 'Mariupol'
                i['city'] = user_city
                return i


class TaskTest2(TestCase):

    def test_search_first_name(self):  # 1
        self.assertEqual(search_first_name(), {'first_name': 'Anton', 'last_name': 'Shalamov',
                                               'full_name': 'Anton Sergijovich Shalamov',
                                               'telephone_number': '0963051160', 'city': 'Rostov-on-Don'})

    def test_search_last_name(self):  # 2
        self.assertEqual(search_last_name(), {'first_name': 'Anton', 'last_name': 'Shalamov',
                                              'full_name': 'Anton Sergijovich Shalamov',
                                              'telephone_number': '0963051160', 'city': 'Rostov-on-Don'})

    def test_search_full_name(self):  # 3
        self.assertEqual(search_full_name(), {'first_name': 'Anton', 'last_name': 'Shalamov',
                                              'full_name': 'Anton Sergijovich Shalamov',
                                              'telephone_number': '0963051160', 'city': 'Rostov-on-Don'})

    def test_search_telephone_number(self):  # 4
        self.assertEqual(search_telephone_number(), {'first_name': 'Anton', 'last_name': 'Shalamov',
                                                     'full_name': 'Anton Sergijovich Shalamov',
                                                     'telephone_number': '0963051160', 'city': 'Rostov-on-Don'})

    def test_search_city(self):  # 5
        self.assertEqual(search_city(), {'first_name': 'Anton', 'last_name': 'Shalamov',
                                         'full_name': 'Anton Sergijovich Shalamov',
                                         'telephone_number': '0963051160', 'city': 'Rostov-on-Don'})

    def test_delete_telephone_number(self):  # 6
        self.assertNotIn(delete_telephone_number(), phonebook_dict['items'])

    def test_add_entry(self):  # 7
        self.assertIn(add_entry(), phonebook_dict['items'])

    def test_update_record(self):  # 8
        self.assertEqual(update_record(), {'first_name': 'Valentin', 'last_name': 'Karkavin',
                                           'full_name': 'Valentin Sergijovich Karkavin',
                                           'telephone_number': '0959119354', 'city': 'Mariupol'})


if __name__ == '__main__':
    main()
