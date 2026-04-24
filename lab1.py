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

x=str(input("Введите x (можно ввести массив через запятую):\n"))
t_list=x.split(',')
l = len(t_list)
t_list_temp=[]
for i in t_list:
    i=float(i)
    t_list_temp.append(i)
#t=0.0
t_list=t_list_temp
i=0
while i!=l: #Цикл для массива
    t = float(t_list[i])
    if t==0:
        z=0
        print("Z("+str(t)+") =", round(z,2))
    if t<0:
        a=9*n.pi*t+10*n.cos(x)
        b=n.sqrt(complex(t))-abs(n.sin(t))
        z=a/b*n.exp(x)
        if n.imag(z)<0:
            print("Z("+str(t)+") =", str(round(n.real(z),2))+'-'+str(round(n.imag(z),2))+'i')    
        else:
            print("Z("+str(t)+") =", str(round(n.real(z),2))+'+'+str(round(n.imag(z),2))+'i')
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