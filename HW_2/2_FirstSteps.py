# Task 1   the python interpreter via the terminal get familiar with running python commands in the terminal,
# work with output, etc.
if __name__ == '__main__':
    print('python')
    print(2+2,'= 4')
    print(2 + 2, 5)
    print(int(2/2))
    print('sasho'.capitalize())

# Task 2 Create a python program named "task2", and use the built - in function 'print' in it
# several times. Try to pass "sep", "end" params and pass several parameters separated by
# commas. Also, provide a comment text above each print statement, mentioned above,
# with the expected output after execution of the particular print statement.
# (Ex. # 'hello world' print("hello world") )

#     q, w, t, y
    print('q','w','t','y',sep=',')

    # 101; 102; 103
    print(101,102,103,sep='; ')

    # 1 3 5....1000
    print(1,3,5,end='....1000\n')

    # second, kilo, meter are measures
    print('second,','kilo,','meter',end=' are measures\n')

    # ivanov.ivan@gmail.com; petro.alekseev@gmail.com; kritikovalex@gmail.com - python group 2023
    print('ivanov.ivan','petro.alekseev','kritikovalex',sep='@gmail.com; ',end='@gmail.com - python group 2023\n')



# Task 3 Write  a program, which has two print statements to print the following text (capital
#letters "O" and "H", made from "#" symbols):
#     #########
#     #       #
#     #       #
#     #       #
#     #########
#
#     #       #
#     #       #
#     #########
#     #       #
#     #       #
# Pay attention that usage of spaces is forbidden, as well as creating the whole result text
# string using """ """, use '\n' and '\t' symbols instead.

    #V.1
    print('\t'+'#'*9,'\n','\t'+'#','\t'*2+'#','\n','\t'+'#','\t'*2+'#','\n','\t'+'#','\t'*2+'#','\n','\t'+'#'*9,'\n'*2)
    print('\t'+'#','\t'*2+'#','\n','\t'+'#','\t'*2+'#','\n','\t'+'#'*9,'\n','\t'+'#','\t'*2+'#','\n','\t'+'#','\t'*2+'#'+'\n')

    # V.2
    a='\t'+'#'*9+'\n'
    b='\t'+'#'+'\t'*2+'#'+'\n'
    print(a+b*3+a+'\n'+b*2+a+b*2)