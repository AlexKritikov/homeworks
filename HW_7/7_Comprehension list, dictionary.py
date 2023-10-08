

if __name__ == '__main__':
# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.
    sentence = input('Please enter your sentence')
    list1_t1 = set(list(sentence.split()))
    list2_t1 = list(sentence.split())
    dict_t1 = {i: list2_t1.count(i) for i in list1_t1}
    print(dict_t1)

 
# Task 2
# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the
# quantity of this exact item.
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    total_price = 0

    for i in stock:
        total_price+=stock[i]*prices[i]
    print(total_price)


# Task 3. List comprehension exercise.
# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
    list_comprehension = [(i,i**2) for i in range(1,11)]
    print(list_comprehension)


# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,"""
    days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_counter=0
    dictionary_week_1 = {days_of_week[i]:i+1 for i in range(len(days_of_week))}
    dictionary_week_2 = {i+1:days_of_week[i] for i in range(len(days_of_week))}
    print(dictionary_week_1)
    print(dictionary_week_2)