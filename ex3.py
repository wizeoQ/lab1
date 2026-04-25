import formatter as f

f.ex(3)

print("Введите через запятую диапазон чисел, который необходимо проверить.")
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
print("Массив -", points,"\nСреди них интервалу [",start,",",end,"] принадлежат:")
for i in points:
    if i>=start and i<=end:
        print(i,end=' , ')
f.eq()