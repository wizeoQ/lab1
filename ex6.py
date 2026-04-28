import formatter as f
import numpy as np
import matplotlib.pyplot as plt

f.ex(6)

#Ввод данных
while True:
    try:
        t=float(input("Введите t\n>"))
        break
    except ValueError:print("Неверный тип данных")

while True:
    try:
        x=float(input("Введите x\n>"))
        break
    except ValueError:print("Неверный тип данных")

while True:
    try:
        a=float(input("Введите a (диапазон 0.1 до 5.0)\n>"))
        if 0.1<=a<=5: break
        else:print("Значения нет в диапазоне.")
    except ValueError: print("Неверный тип данных")

f.eq()