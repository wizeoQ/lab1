import formatter as f
import numpy as np
import matplotlib.pyplot as plt
f.ex(3)
#---Ввод данных---
print("Введите через запятую диапазон чисел, который необходимо провести")
while True:
    try:
        points=list(map(float,input(">").split(',')))
        break
    except (ValueError, TypeError):
        print("Неправильный тип данных.")

f.l()

print("Введите начало диапазона, в котором будет проверка.")
while True:
    try:
        start=float(input(">"))
        break
    except (ValueError, TypeError):
        print("Неправильный тип данных.")

f.l()

print("Введите конец диапазона, в котором будет проверка.")
while True:
    try:
        end=float(input(">"))
        break
    except (ValueError, TypeError):
        print("Неправильный тип данных.")
if start>end:
    start,end=end,start

f.l()

calc_out=[]
calc_index=[]

i=0
while i!=len(points):
    if start<=points[i]<=end:
        calc_out.append(points[i])
        calc_index.append(i)
    i+=1
    
if len(calc_out)==0:
    print("В заданном диапазоне значений нет.")
else:
    #---Проверка на принадлежность массиву---
    print("Массив:\n",points,"\n\nСреди них отрезку [",start,",",end,"] принадлежат:\n",sep='')
    for i,j in zip(calc_out,calc_index):
        print(i,'(',j,')',sep='')
    
    f.l()
    
    #---Сортировка данных---
    print("Сортировка массива:")
    sort=np.sort(calc_out)
    sort_temp=list(np.argsort(calc_out))
    sort_index = list('w'*len(sort))
    i=0
    while i!=len(calc_out):
        a=sort_temp.index(i)
        sort_index[a]=calc_index[i]
        i+=1
    del a,sort_temp
    i=0
    while i!=len(sort):
        print(sort[i],'(',sort_index[i],')',sep='')
        i+=1
            
    f.eq()

    #---Вывод графика
    labels=[]
    for i,j in zip(sort,sort_index):
        if float(i)==int(i):
            i=int(i)
        x=i/100
        e=2
        if x%10==0 and i!=0:
            while x%10==0:
                e+=1
                x=x/10
            i=str(int(x))+'e'+str(e)
        labels.append(str(round(i,2))+'('+str(j)+')')

    df=sort[-1]-sort[0] #Длина сортировки
    plt.axhline(y=0,color='red') #Вся ось (красная)
    plt.axvline(x=0,color='grey',linestyle='--',alpha=0.25)
    if len(sort)==1:
        plt.axis([-0.1*(end-start),end+0.1*(end-start),-1,1])
    else:
        plt.axis([sort[0]-0.1*df,sort[-1]+0.1*df,-1,1])
    plt.hlines(0,start,end,color='black') #Область допустимых значений
    plt.plot(sort,np.linspace(0,0,len(sort)),'go')
    for i,j in zip(sort,labels):
        plt.text(i,0.07,j,horizontalalignment='center',fontsize=10)
    plt.show()
    
    del i,j