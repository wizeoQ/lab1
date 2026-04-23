#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:52:33 2026

@author: wizeo
"""
class r():
    def z(number):
        print("\n==========")
        print("Задание ", number)
    def t(tire=5):
        i=0
        print('')
        while i!=tire:
            print("-", end='')
            i+=1
        print('')
    def r(ravno=5):
        i=0
        print('')
        while i!=ravno:
            print("=", end='')
            i+=1
        print('')

r.z(1)

name = input ("Ваши имя, фамилия, отчество?\n\t> ")
age = input ("Сколько Вам лет?\n\t> ")
place = input ("Где Вы живёте?\n\t> ")

r.t(3)

print("Ваши ФИО -", name, end="\n")
print("Ваш возраст -", age, end="\n")
print("Вы живёте в -", place, end="")

r.r()