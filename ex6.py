import formatter as f
import numpy as np
import matplotlib.pyplot as plt

f.ex(6)

#Вывод формулы
print("\n          / a*[(5pi*t)^2+3cos(2x)] \\")
print("Z(t,x,a)= |────────────────────────| * beta")
print("          \\    ln(|t|+1-sin(t)^2   /")
print("\n, где beta - e^(-ax)+sqrt(at)")
f.l()
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
#Крайние случаи
if len(list(t))==1 and t[0]==0:print("Деление на ноль.")
#Расчёт выражения.
else:
    z=[]
    for t_i in t:
        if t_i==0:z.append(np.nan)
        else:
            nmrtr=a*((5*np.pi*(t_i**2))+3*np.cos(2*x))
            dnmtr=np.log(abs(t_i)+1)-np.sin(t_i)**2
            answ=nmrtr/dnmtr*np.exp(-a*x)+np.sqrt(complex(a*t_i))
            z.append(answ)
    #Вывод данных.
    print("Вывести данные? Y/N",end='')
    while True:
        out_flag=input('>')
        f.l()
        if out_flag=="":continue
        if out_flag in "yY1дД":
            print("Z(t, x, a)= ...")
            for t_i,z_i in zip(t,z):
                if float(a)==int(a):a=int(a) #константа a
                if float(x)==int(x):x=int(x) #константа x
                if float(t_i)==int(t_i):t_i=int(t_i) #убираем лишний .0
                if t_i==0:z_ir,z_ii="nan",'' #случай nan
                else:
                    z_ir=round(float(np.real(z_i)),3)
                    z_ii=round(float(np.imag(z_i)),3)
                    if float(z_ir)==int(z_ir):z_ir=int(z_ir) #убираем лишний .0
                    if float(z_ii)==int(z_ii):z_ii=int(z_ii) #убираем лишний .0
                    if z_ii==0:z_ii='' #число не мнимое
                    elif z_ii>0:z_ii='+'+str(z_ii)+'i'
                    elif z_ii<0:z_ii=str(z_ii)+'i' #минус сам допишется
                print("Z(",t_i,", ",x,", ",a,") = ",z_ir,z_ii,sep='')
            break
        if out_flag in "nN0нН":break