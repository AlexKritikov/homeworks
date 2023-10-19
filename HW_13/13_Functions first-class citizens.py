if __name__ == '__main__':

# Task 1.Write a Python program to detect the number of local variables declared in a function.

    def local_var_detect(func_t1):
        return func_t1.__code__.co_nlocals

# Task 2.
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

    def inside_func(value):
        print(f'The value of inside function is {value} ')
    def func_t2(value):
            if value>0:
                return inside_func(value*1000)
            else:
                print('The end')

# Task 3
#
# Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside the list
# are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the
# second one
#
# def choose_func(nums: list, func1, func2):
#     pass
#
# # Assertions
#
# nums1 = [1, 2, 3, 4, 5]
#
# nums2 = [1, -2, 3, -4, 5]
#
#
# def square_nums(nums):
#
#     return [num ** 2 for num in nums]
#
# def remove_negatives(nums):
#
#     return [num for num in nums if num > 0]
#
#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
#
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]""""
    nums=[1, 2, 3, 4 ,5]
    def square_nums():
        return [num**2 for num in nums]
    def remove_negatives():
        return list(filter(lambda num:num>=0,nums))
    def choose_func():
        count=0
        if sum([count+1 for i in nums if i<0])>0:
            return remove_negatives()
        else:
            return square_nums()
