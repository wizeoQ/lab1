#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import formatter as f
import numpy as n

#f.ex(1)
#
#name = input ("Ваши имя, фамилия, отчество?\n\t> ")
#age = input ("Сколько Вам лет?\n\t> ")
#place = input ("Где Вы живёте?\n\t> ")
#
#f.d()
#
#print("Ваши ФИО -", name, end="\n")
#print("Ваш возраст -", age, end="\n")
#print("Вы живёте в -", place, end="")

f.ex(2)

print("\n    9*pi*t+10cos(x)")
print("Z = ──────────────── * e^x")
print("    sqrt(t)-|sin(t)|")

f.l(5)

x=float(input("Введите x - "))
t_list=[4,-6,1.5,6,-15,4,18,-9]
l = len(t_list)
#t=0.0
i=0
while i!=l: #Цикл для массива
    t = float(t_list[i])
    if t==0:
        z=0
        print("Z("+str(t)+") =", round(z,2))
    if t<0:
#       print("Z("+str(t)+") =", round(n.real(z),2)+'i'+round(n.imag(z),2))
        print("Z("+str(t)+") = Комплексное число")
    else:
        a=9*n.pi*t+10*n.cos(x)
        b=n.sqrt(t)-abs(n.sin(t))
        z=a/b*n.e**x
        print("Z("+str(t)+") =", round(z,2))
    i+=1
    
#while t!=11: #Цикл для одного значения
#    if t==0:
#        z=0
#        print("Z("+str(int(t))+") =", round(z,2))
#    else:
#        a=9*n.pi*t+10*n.cos(x)
#        b=n.sqrt(t)-abs(n.sin(t))
#        z=a/b*n.e**x
#        print("Z("+str(int(t))+") =", round(z,2))
#    t+=1