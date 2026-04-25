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
    while True:
        try:
            x=float(input("Введите x > "))
            break
        except ValueError:
            print("Неверный тип данных.")
    print("Введите t")
    print("Если хотите ввести массив - вводите через запятую")
    print("Если нужен диапазон, введите \"d\"",end="")
    t=""
    while True:
        try:
            t=str(input("t > "))
            if t=='d':
                break
            #-----Проверка t    
            t=t.replace(' ','')
            t=t.split(',')
            t=list(map(float,t))
            elements_output='Y'
            break
        except ValueError:
            print("Неверный тип данных.")
    f.l(5)
    #----------Построение диапазона----------
    '''linspace используется трижды как индикатор того,
    что пользователь ввёл правильнй тип данных (т.к.
    для points помимо значения float нужно также >=0'''
    
    if t=='d':
        while True:
            try:
                start = float(input("Введите старт массива > "))
                t=np.linspace(start,0,1)
                break
            except ValueError:
                print("Неверный тип данных.")
        while True:
            try:
                end = float(input("Введите конец массива > "))
                t=np.linspace(start,end,1)
                break
            except ValueError:
                print("Неверный тип данных.")
        while True:
            try:
                points = int(input("Введите количество элементов > "))
                t=np.linspace(start,end,points)
                break
            except ValueError:
                print("Неверный тип данных")
                print("или число точек отрицательное.")
        #-------Нужен ли вывод значений-------
        print("Нужен ли вывод ответов?")
        print("Предупреждение: Их может быть много.")
        elements_output = input("Y/N > ")
        #=------------------------------------
        if points==0:
            print("Элементы отсутствуют.")
            t=[]        
    #------------------Блок вычислений----------------
    z=[]
    i=0
    while i!=len(t):
        if t[i]==0:
            ans=np.nan
            if elements_output=='Y' or elements_output=='y':
                print("Z(0.0) = nan")
        else:
            a=9*np.pi*t[i]+10*np.cos(x)
            b=np.sqrt(complex(t [i]))-abs(np.sin(t[i]))
            ans=a/b*np.exp(x) #ans - float значение внутри z
            if elements_output=='Y' or elements_output=='y':
                if np.imag(ans)<0:
                    print("Z("+str(round(t[i],2))+") =", str(np.round(np.real(ans),2))+str(np.round(np.imag(ans),2))+'i')    
                elif np.imag(ans)>0:
                    print("Z("+str(round(t[i],2))+") =", str(np.round(np.real(ans),2))+'+'+str(np.round(np.imag(ans),2))+'i')
                else:
                    print("Z("+str(round(t[i],2))+") =", str(np.real(np.round(ans,2))))
        z.append(ans)
        i+=1
    #------------------Вывод графика----------------
    choice=input("Вывести график? \nY/N > ")
    if choice=='y' or choice=='Y':
        plt.plot(np.round(t,2),np.round(np.real(z),2),'|r-')
        plt.plot(np.round(t,2),np.round(np.imag(z),2),'|b:')
        plt.legend(['Re(Z)','Im(Z)'])
        plt.title("Зависимость Z от t")
        plt.xlabel("t")
        plt.ylabel("Z(t)")
        plt.grid()
        plt.show()
    else:
        pass
    f.l(5)