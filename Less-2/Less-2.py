"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""
m = int(input("Введите количество монеток, n - "))
x = int(input("Введите количество монеток вверх гербом, x - "))
y = int(input("Введите количество монеток вверх решкой ,y - "))
if x + y == m:
    if x < y:
        print(f"вверх гербом меньше, нужно перевернуть - {x} монеток")
    elif x == y:
        print(
            f"количество монет гербом и решкой одинаково, можно перевернуть - {x} гербы или решки {y}"
        )
    else:
        print(f"вверх решкой меньше, нужно перевернуть - {y} монеток")
else:
    print("Введенные данные некорректны")

"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа."""
import math

x1 = 0
y1 = 0
s = int(input("Введите сумму искомых чисел, сумма - "))
p = int(input("Введите произведение искомых чисел, произведение - "))
for x1 in range(1, 1000):
    for y1 in range(1, 1000):
        if (s == x1 + y1) and (p == x1 * y1):
            print(f"первое число = {x1} , второе число = {y1}")

# " способ - решение с использованием квадратного уравнения
d = s**2 - 4 *(-p)*(-1)
print ("d = ", d)
x3 = (-s + round(math.sqrt(d))) / (2 * (-1))
x4 = (-s - round(math.sqrt(d))) / (2 * (-1))

print(f"x3 = {x3}")
print(f"x4 = {x4}")
'''if (x1 > 0): 
    if(y + x1 == s and y * x1 == p):
       print(f"X =  {x1} , Y = {y}")
elif (x2 > 0) :
    if (y + x2 == s and y * x2 == p):
    # y = summ - x2
        print(f"X =  {x2} , Y = {y}")'''

"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""
n = int(input("Введите число N - "))
for i in range(1, n):
    digit = 2**i
    if digit <= n:
        print(digit)
