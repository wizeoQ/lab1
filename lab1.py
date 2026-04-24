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
print("Введите t")
print("Если хотите ввести массив - вводите через запятую")
print("Если нужен диапазон, введите \"d\"",end="")
t=str(input("\t> "))
f.l(5)
#------------------Построение диапазона----------------
if t=='d':
    start = float(input("Введите старт массива > "))
    end = float(input("Введите конец массива > "))
    points = int(input("Введите количество элементов > "))
    if points<=0:
        print("Элементы отсутствуют.")
        t='0'
    elif points==1:
        t=str(n.average([start,end]))
    elif points==2:
        t=str(str(start)+','+str(end))
    else:
        print("пока ничего")
        t='0'
#------------------Построение диапазона----------------
t.replace(' ','')
t_list=t.split(',')
l = len(t_list)
t_list_temp=[]
for i in t_list:
    i=float(i)
    t_list_temp.append(i)
t_list=t_list_temp

#------------------Блок вычислений----------------
i=0
while i!=l:
    t = float(t_list[i])
    if t==0:
        z=0
        print("Z("+str(t)+") =", round(z,2))
    elif t<0:
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
#------------------Блок вычислений----------------