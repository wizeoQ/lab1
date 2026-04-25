import formatter as f

f.ex(3)

a=[1,2,5]
print("Массив -", a,"\nСреди них интервалу [1,3] принадлежат:")
for i in a:
    if i>=1 and i<=3:
        print(i,end=' ')
f.eq()