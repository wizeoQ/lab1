#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import formatter as f
import numpy as n

f.ex(1)

name = input ("Ваши имя, фамилия, отчество?\n\t> ")
age = input ("Сколько Вам лет?\n\t> ")
place = input ("Где Вы живёте?\n\t> ")

f.d()

print("Ваши ФИО -", name, end="\n")
print("Ваш возраст -", age, end="\n")
print("Вы живёте в -", place, end="")

f.ex(2)

print("\n    9*pi*t+10cos(x)")
print("Z = ──────────────── * e^x")
print("    sqrt(t)-|sin(t)|")

f.l(5)

x=float(input("Введите x - "))
t=float(input("Введите t - "))

a=9*n.pi*t+10*n.cos(x)
b=n.sqrt(t)-abs(n.sin(t))
z=a/b*n.e**x

print("\nОтвет: Z =", round(z,2))