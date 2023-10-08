# Task 1. The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
if __name__ == '__main__':
    import random
    counter_task1 = 0
    list_numbers_t1=[]
    while counter_task1<10:
        list_numbers_t1.append(random.randint(0,1000))
        counter_task1+=1
    print(min(list_numbers_t1))


# Task 2. Exclusive common numbers.
# Generate 2 lists with the lengtgh of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
    counter_task2 = 0
    list_numbers_1_t1 = []
    list_numbers_2_t2 = []
    while counter_task2 < 10:
        list_numbers_1_t1.append(random.randint(0, 10))
        list_numbers_2_t2.append(random.randint(0, 10))
        counter_task2 += 1
    print(set(list_numbers_1_t1).intersection(list_numbers_2_t2))


# Task 3. Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible
# by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
    counter_1_task3 = 1
    element=0
    list_numbers_1_t3 = []
    special_list=[]
    while counter_1_task3<=100:
        list_numbers_1_t3.append(counter_1_task3)
        counter_1_task3+=1
    while element<len(list_numbers_1_t3):
        if list_numbers_1_t3[element]%7==0 and list_numbers_1_t3[element]%5!=0:
            special_list.append(list_numbers_1_t3[element])
            element+=1
        else:
            element+=1
    print(special_list)
