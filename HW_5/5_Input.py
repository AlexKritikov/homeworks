import random

if __name__ == '__main__':
# Task 1.The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    while True:
        game_number = str(random.randint(1, 10))
        player_number = input('Choose number between 1 and 10')
        if player_number == 'No':
            break
        elif player_number.isdigit()==True and int(player_number) <= 10 and int(player_number) >= 1:
            if player_number==game_number:
                print('Congratulations! Yo win')
            else:
                print('Sorry.You lose')
        else:
            print('You should choose only numbers between 1 and 10')
            continue


# Task 2. The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    name = input('Insert your name please')
    while True:
        age=input('Insert your age please')
        if age.isdigit()==True:
            print(f'Hello {name}, on your next birthday you’ll be {int(age)+1} years')
            break
        else:
            print('Choose only numerical symbols inserting your age')
            continue


# Task 3. Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
# string.# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    words_count=0
    user_word = input('Please enter any word')
    while words_count < 5:
        symbols = []
        for i in user_word:
            symbols.append(i)
        random_word = ''
        while len(random_word) < len(user_word):
            chr_random = random.randint(0, len(user_word) - 1)
            if symbols[chr_random] == '':
                continue
            else:
                random_word+=symbols[chr_random]
                symbols.pop(chr_random)
                symbols.insert(chr_random, "")
        print(random_word)
        words_count += 1