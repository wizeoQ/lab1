#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import formatter as f

f.ex(1)

name = input ("Ваши имя, фамилия, отчество?\n\t> ")
age = input ("Сколько Вам лет?\n\t> ")
place = input ("Где Вы живёте?\n\t> ")

f.d(3)

print("Ваши ФИО -", name, end="\n")
print("Ваш возраст -", age, end="\n")
print("Вы живёте в -", place, end="")

f.eq()