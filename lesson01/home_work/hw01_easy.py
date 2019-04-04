
#-*- coding: utf-8 -*-
__author__ = 'Kirichenko Maxim Evgen\'evich'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
while True:
    try:
        a = input('Enter a number: ')    
        a = int(a)
        break
    except NameError:
        print('You supposed to enter any number, but you entered the letters, try again!')
    except SyntaxError:
        print('You have to entered digital and literal mix. You supposed to enter only digitals. Try again!')
counter = 0
while counter<len(str(a)):
    print(str(a)[counter])
    counter+=1
print('Everithing well. Thank you. Have a nice day!')



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

while True:
    try:
        a = input('Enter a 1st number: ')
        a = int(a)
        
        b = input('Enter a 2nd number: ')
        b = int(b)
        break
    except NameError:
        print('You supposed to enter any number, but you entered the letters, try again!')
    except SyntaxError:
        print('You have to entered digital and literal mix. You supposed to enter only digitals. Try again!')

a, b = b, a
print('a = {}; b = {}'.format(a,b))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
while True:
    try:
        a = input('How old are you: ')
        a = int(a)
        break
    except NameError:
        print('You supposed to enter how old you are. Just digitals. Try again!')
    except SyntaxError:
        print('You have to entered digital and literal mix. You supposed to enter only digitals. Try again!')
if a>=18:
    print('Access granted')
else:
    print('Access not granted. Sorry, this request allowed to use only for adult person')
