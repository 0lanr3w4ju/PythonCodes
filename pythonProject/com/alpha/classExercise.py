x = 2
y = 3
print('***********************')
print('answer to question 1')
print('***********************')
print('x =', x)  # 1.1
print('value of', x, '+', x, 'is', (x + x))  # 1.2
print('x =')  # 1.3
print((x + y), 'x =', (y + x))  # 1.4  # ------------ # 1

print('***********************')
print('answer to question 2')
print('***********************')
rating1 = input('enter an integer rating between 1 and 10: ')  # this passes a string
rating = int(rating1)  # string has been converted using the int() function
print(type(rating1))  # this is data type string
print(type(rating))  # this is data type integer  # ------------ # 2

print('***********************')
print('answer to question 3')
print('***********************')
grade = 91
if grade >= 90:
    print(f'Congratulations! your grade of {grade} earns you an A in this course')  # ------------ # 3

print('***********************')
print('answer to question 4')
print('***********************')
print('27.5 + 2 =', 27.5 + 2)
print('27.5 - 2 =', 27.5 - 2)
print('27.5 * 2 =', 27.5 * 2)
print('27.5 / 2 =', 27.5 / 2)
print('27.5 // 2 =', 27.5 // 2)
print('27.5 ** 2 =', 27.5 ** 2)  # ------------ # 4

print('***********************')
print('answer to question 5')
print('***********************')
r = 2

print('diameter =', 2 * r)
print('circumference =', 2 * 3.14159 * r)
print('area =', 3.14159 * r ** 2)  # ------------ # 5

print('***********************')
print('answer to question 6')
print('***********************')
integer = int(input('integer = '))

if 2 % integer == 0:
    print(f'{integer} is an evEn nuMbeR')
else:
    print(f'{integer} is an Odd nuMbeR') # ------------ # 6

print('***********************')
print('answer to question 7')
print('***********************')
if 1024 % 4 == 0:
    print('1024 is a multiple of 4')
else:
    print('1024 is not a multiple of 4')

if 2 % 10 == 0:
    print('10 is a multiple of 2')
else:
    print('10 is not a multiple of 2')

