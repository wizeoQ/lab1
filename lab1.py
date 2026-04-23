#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:52:33 2026

@author: wizeo
"""
def D(n):
    if n == 1:
        print("\n-----\n")
    elif n == 2:
        print("\n=========\n")
    else:
        print('\n---\n')

name = input ("Ваши имя, фамилия, отчество?\n\t> ")
age = input ("Сколько Вам лет?\n\t> ")
place = input ("Где Вы живёте?\n\t> ")

D(1)

print("Ваши ФИО -", name, end="\n")
print("Ваш возраст -", age, end="\n")
print("Вы живёте в -", place, end="")

D(2)