"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""
n= int (input('Введите количество монеток, n - '))
x= int (input('Введите количество монеток вверх гербом, x - '))
y= int (input('Введите количество монеток вверх решкой ,y - '))
if x + y == n:
    if x < y:
        print(f"вверх гербом меньше, нужно перевернуть - {x} монеток")
    else:
        print(f"вверх решкой меньше, нужно перевернуть - {y} монеток")
else:
    print('Введенные данные некорректны')