import formatter as f
import numpy as np
import matplotlib.pyplot as plt

def run_exercise_2():
    f.ex(2)
    #-------------Вывод формулы--------------
    print("\n    9*pi*t+10cos(x)")
    print("Z = ──────────────── * e^x")
    print("    sqrt(t)-|sin(t)|")
    f.l(5)
    #-------------Ввод данных----------------    
    x=float(input("Введите x > "))
    print("Введите t")
    print("Если хотите ввести массив - вводите через запятую")
    print("Если нужен диапазон, введите \"d\"",end="")
    t=str(input("t > "))
    f.l(5)
    #----------Построение диапазона----------
    if t=='d':
        start = float(input("Введите старт массива > "))
        end = float(input("Введите конец массива > "))
        points = int(input("Введите количество элементов > "))
        elements_output = input("Нужен ли вывод ответов? Их может быть много. Y/N > ")
        if start>end:
            temp=end
            end=start
            start=temp
            
        if points<=0:
            print("Элементы отсутствуют.")
            t='0'
        elif points==1:
            t=str(np.average([start,end]))
        elif points==2:
            t=str(str(start)+','+str(end))
        else:
            inter=((end-start)/(points-1))
            t=[]
            t.append(start)
            t.append(',')
            i=1
            while i<(points-1):
                t.append(round(inter*i+start,2))
                t.append(',')
                i+=1
            t.append(end)
            temp=''
            for i in t:
                temp = temp+str(i)
            t=temp
            #t=str(str(start)+','+str(inter)+','+str(end))
    #-----Перевод строки в лист вещественных значений--
    t=t.replace(' ','')
    t_list=t.split(',')
    l = len(t_list)
    t_list_temp=[]
    for i in t_list:
        i=float(i)
        t_list_temp.append(i)
    t_list=t_list_temp
    #------------------Блок вычислений----------------
    z_list=[]
    i=0
    while i!=l:
        t = float(t_list[i])
        if t==0:
            z=0
            if elements_output=='Y' or elements_output=='y':
                print("Z("+str(t)+") =", round(z,2))
        else:
            a=9*np.pi*t+10*np.cos(x)
            b=np.sqrt(complex(t))-abs(np.sin(t))
            z=a/b*np.exp(x)
            if elements_output=='Y' or elements_output=='y':
                if np.imag(z)<0:
                    print("Z("+str(t)+") =", str(np.round(np.real(z),2))+'-'+str(np.round(np.imag(z),2))+'i')    
                elif np.imag(z)>0:
                    print("Z("+str(t)+") =", str(np.round(np.real(z),2))+'+'+str(np.round(np.imag(z),2))+'i')
                else:
                    print("Z("+str(t)+") =", str(np.round(z,2)))
        z_list.append(np.round(z,2))
        i+=1
    #------------------Вывод графика----------------
    choise=input("Вывести график? Y/N > ")
    if choise=='y':
        plt.plot(t_list,np.real(z_list))
        plt.xlabel("t")
        plt.ylabel("Z(t)")
        plt.show()
    else:
        pass
    f.l(5)