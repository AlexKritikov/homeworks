if __name__ == '__main__':
    # Task 1. A Person class
    # Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as
    # attributes. Make another method called talk() which makes prints a greeting from the person containing, for example
    # like this: "Hello, my name is Carl Johnson and I’m 26 years old".
    class Person():
        def __init__(self,firstname,lastname,age:int):
            self.firstname=firstname
            self.lastname = lastname
            self.age=age
        def talk(self):
            print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old" )

# Task 2.Doggy age.
# Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

    class Dog():
        age_factor=7
        def __init__(self,dog_age:int):
            self.dog_age=dog_age
        def human_age(self):
            print(f'This dog is {Dog.age_factor*self.dog_age} human years old')

# Task 3. TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.
#
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
#

    CHANNELS=["BBC", "Discovery", "TV1000", "Eurosport", "MTV" ]

    class TVController():
        def __init__(self,CHANNELS:list):
            self.channels=CHANNELS
            self.channel_number = 0

        def first_channel(self):
            self.channel_number = 0
            return self.channels[self.channel_number]

        def last_channel(self):
            self.channel_number = len(self.channels) - 1
            return self.channels[self.channel_number]

        def turn_channel(self,N: int):
            if N > len(self.channels):
                raise ValueError("We don't have so many channels!")
            else:
                self.channel_number = N - 1
                return self.channels[self.channel_number]

        def next_channel(self):
            if self.channel_number == len(self.channels) - 1:
                return self.first_channel()
            else:
                self.channel_number += 1
                return self.channels[self.channel_number]

        def previous_channel(self):
            if self.channel_number == 0:
                return self.last_channel()
            else:
                self.channel_number -= 1
                return self.channels[self.channel_number]

        def current_channel(self):
            return self.channels[self.channel_number]

        def exists(self,N):
            if isinstance(N, int) == True and 0 < N <= len(self.channels):
                return ('Yes')
            elif isinstance(N, str) == True and N in self.channels:
                return ('Yes')
            else:
                return ('No')










