import formatter as f
import numpy as np
import matplotlib.pyplot as plt

def run_exercise_6():
    f.ex(6)
    
    #Вывод формулы
    print("\n          / a*[(5pi*t)^2+3cos(2x)] \\")
    print("Z(t,x,a)= |────────────────────────| * beta")
    print("          \\    ln(|t|+1)-sin(t)^2  /")
    print("\n, где beta - e^(-ax)+sqrt(at)")
    f.l()
    #Ввод данных
    print("Введите t\nДля ввода массива используйте запятые.",end="")
    print("Для ввода диапазона введите d.",end="")
    t=input(">")
    
    #Ввод диапазона
    if t!='d':
        try:
            t=list(map(float,(t.split(','))))
        except ValueError:
            print("\nНеверный тип данных\nВведите t",end="")
            while True:
                try:
                    t=input('>')
                    if t=='d':break
                    t=list(map(float,t.split(',')))
                    break
                except ValueError:print("Неверный тип данных")
        points=1
    #Ввод t
    if t=='d':
        t=0
        while True:
            try:
                start=float(input("Введите начало массива\n>"))
                break
            except ValueError:print("Неверный тип данных\n>")
        while True:
            try:
                end=float(input("Введите конец массива\n>"))
                break
            except ValueError:print("Неверный тип данных.")
        while True:
            try:
                points=int(input("Введите количество элементов\n>"))
                t=np.linspace(start,end,points)
                break
            except (ValueError, TypeError):print("Неверный тип данных или отрицательное значение.")
    
    #Крайние случаи       
    if len(list(t))==1 and t[0]==0:print("Деление на ноль.")
    elif points==0:print("Значения отсутствуют.")
    
    #Расчёт выражения.
    else:
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
        z=[]
        for t_i in t:
            if t_i==0:z.append(np.nan)
            else:
                nmrtr=a*((5*np.pi*(t_i**2))+3*np.cos(2*x))
                dnmtr=np.log(abs(t_i)+1)-np.sin(t_i)**2
                answ=nmrtr/dnmtr*np.exp(-a*x)+np.sqrt(complex(a*t_i))
                z.append(answ)
        #Вывод данных.
        def out_z():
            f.l()
            print("Z(t, x, a)= ...")
            x_out=f.simple_complex(x,3,0)
            a_out=f.simple_complex(a,3,0)
            for t_i,z_i in zip(t,z):
                t_out=f.simple_complex(t_i,3,0)
                z_out=f.simple_complex(z_i,3,0)
                print("Z(",t_out,", ",x_out,", ",a_out,") = ",z_out,sep='')
        print("Вывести данные? Y/N",end='')
        f.yes_or_not(out_z)
        #Построение графика
        def graph():
            plt.plot(t,np.real(z),'-r')
            plt.plot(t,np.imag(z),'-g')
            plt.xlabel("t")
            plt.ylabel("Z(t)")
            plt.title("Зависимость Z от t")
            plt.legend(["Re(Z)","Im(Z)"])
            plt.show()
        print("Вывести график? Y/N",end='')
        f.yes_or_not(graph)
        
run_exercise_6()