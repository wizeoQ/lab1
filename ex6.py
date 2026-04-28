import formatter as f
import numpy as np
import matplotlib.pyplot as plt

f.ex(6)

#Ввод данных
print("Введите t\nДля ввода массива используйте запятые.",end="")
while True:
    try:
        t=list(map(float,(input(">").split(','))))
        break
    except ValueError:print("\nНеверный тип данных\nВведите t",end="")

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
    
f.l()
