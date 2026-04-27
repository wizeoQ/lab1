import formatter as f
import numpy as np
import matplotlib.pyplot as plt
f.ex(3)
#---Ввод данных---
#print("Введите через запятую диапазон чисел, который необходимо провести")
#while True:
#    try:
#        points=list(map(float,input(">").split(',')))
#        break
#    except (ValueError, TypeError):
#        print("Неправильный тип данных.")
#
#f.l()
#
#print("Введите начало диапазона, в котором будет проверка.")
#while True:
#    try:
#        start=float(input(">"))
#        break
#    except (ValueError, TypeError):
#        print("Неправильный тип данных.")
#
#f.l()
#
#print("Введите конец диапазона, в котором будет проверка.")
#while True:
#    try:
#        end=float(input(">"))
#        break
#    except (ValueError, TypeError):
#        print("Неправильный тип данных.")
#if start>end:
#    start,end=end,start

f.l()

points=[12,6,2,1,3,7,10,0,5,9]
start=-1.0
end=7.5
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
    i=0
    while i!=len(sort):
        print(sort[i],'(',sort_index[i],')',sep='')
        i+=1
            
    f.eq()
    
    #---Вывод графика
    df=sort[-1]-sort[0] #Длина сортировки
    plt.axhline(y=0,color='red') #Вся ось (красная)
    plt.axvline(x=0,color='grey',linestyle='--',alpha=0.25)
    plt.axis([start-0.1*df,end+0.1*df,-1,1]) #Масштаб осей
    plt.hlines(0,start,end,color='black') #Область допустимых значений
    plt.plot(sort,np.linspace(0,0,len(sort)),'go')
    for i,j in zip(sort,sort_index):
        plt.text(i,0.07,(str(i)+'('+str(j)+')'),horizontalalignment='center')
    plt.show()