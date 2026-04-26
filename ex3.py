import formatter as f
import numpy as np

f.ex(3)
##---Ввод данных---
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

points=[12,6,1,3,7,10,0,5,9]
start=-6.0
end=7.0

#---Проверка на принадлежность массиву---
print("Массив:\n",points,"\n\nСреди них отрезку [",start,",",end,"] принадлежат:\n",sep='')
i=0
calc_out=[]
calc_index=[]
while i!=len(points):
    if start<=points[i]<=end:
        calc_out.append(points[i])
        calc_index.append(i)
        print(points[i],'(',i,')',sep='')
    i+=1

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