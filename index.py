print('hello world!')
# print is a funnction in python 

# variables

age = 20
price = 19.95
first_name = 'solomon'
# print(age)

# boolean
is_online = True

# exercise
patients_name = 'john smith'
patients_age = 20
patients_status = 'new' 

# name = input('what is your name? ')
# print('hello ' + name)

# type conversion
int()
float()
bool()
str()

birth_year = input('enter your birth year: ')
age = 2024 - int(birth_year)
print(age)


# exercise 2
first_num = 90
second_num = 60.1
Sum = input(first_num + second_num)
print(Sum)


# strings
course = 'pyhton for beginners'

# .find()
# to find a given value or string in the str
# .replace()
#  to replace a given str into another


# arithmetic operators
# //, *, +, -, /, %, **

# augumented assignment operator
x = 10
x = x + 3
# or
x += 3

# the two are basically the same


# comparison operators 
x = 3 > 2
print(x)

# >
# >=
# <
# <=
# ==
# !=


# logical operators
price = 25
# and
print(price > 10 and price < 30)
# or
print(price > 10 or price < 30)
# not
print(not price > 30)

temp = 35
if temp > 30:
    print('its a hot day')
elif temp < 10:
    print('its an nice day')
print('done')    


# while loops
i = 1
while i <= 5_100:
    print(i * 'tomi')
    i += 1