import numpy as np

def ex(exercize_number):
    """
    Выводит в консоль упражнение с указанным в аргументе номером.
    """
    print("\n==========")
    print("Задание ", exercize_number)
def eq(equal_quantity=5):
    """
    Выводит в консоль знак "=" в количестве, указанном в аргументе.
    """
    print('\n'+"="*equal_quantity)
def d(dash_quantity=5):
    """
    Выводит в консоль знак "-" в количестве, указанном в аргументе.
    """
    print('\n'+"-"*dash_quantity)
def n():
    """
    Выводит в консоль:༺•༻
    """
    print("\n༺•༻")
def l(line=5):
    """
    Выводит в консоль знак "─" в количестве, указанном в аргументе.
    """
    print('─'*line)
def ln():
    """
    Выводит в консоль ───────✧───────
    """
    print("\n───────✧───────")
    
def yes_or_not(Function_yes=lambda:None,Function_not=lambda:None):
    """
    . . .
    yes_or_not(Func_yes,Func_not)
    Даёт пользователю в консоли выбор между двумя функциями, заданными в аргументе.
    В случае ввода "Y"(или y,д,Д,1) (Yes) - выполняется функция из первого аргумента.
    В случае ввода "N"(или n,н,Н,0)(No) - выполняется функция из второго аргумента.
    По умолчанию в обоих случаях функции ничего не делают.
    """
    while True:
        out_flag=input('>')
        if out_flag=="":continue
        elif out_flag in "yY1дД":
            Function_yes()
            break
        elif out_flag in "nN0нН":
            Function_not()
            break

def simple_complex(x,round_digitals=3,is_print=False,is_i=True,is_return=True):
    """
    return result
    Преобразует комплексное число в удобно-читаемую строку.
    В случае nan и inf выводит соответствующее сообщение.
    x - комплексное число
    round_digitals - число знаков для округления
    is_print - выводить ли строку в консоль
    is_i - обозначение мнимой единицы:
        True - Математическая - "i"
        False - Инженерная - "j"
    is_return - возвращать ли строку в result
    """
    rnd=int(round_digitals)
    if is_i==True:unit='i'
    if is_i==False:unit='j'
    if np.isnan(x)==True:x_ir,x_ii="nan",'' #случай nan
    elif np.isinf(x)==True:x_ir,x_ii="inf",'' #случай inf
    else:
        x_ir=round(float(np.real(x)),rnd)
        x_ii=round(float(np.imag(x)),rnd)
        if float(x_ir)==int(x_ir):x_ir=int(x_ir) #убираем лишний .0
        if float(x_ii)==int(x_ii):x_ii=int(x_ii) #убираем лишний .0
        if x_ii==0:x_ii='' #число не мнимое
        elif x_ii>0:x_ii='+'+str(x_ii)+unit
        elif x_ii<0:x_ii=str(x_ii)+unit #минус сам допишется
    result=str(x_ir)+str(x_ii)
    if is_print==True:print(result)
    if is_return==True:return result
    

def multi_input():
    """
    Даёт возможность определить в консоли переменную как значение, массив или диапазон np.linspace.
    Возвращает list(float)
    """    
    #Ввод данных
    print("Для ввода массива используйте запятые.",sep="")
    print("Для ввода диапазона введите d.",end="")
    x=input(">")
    #Ввод диапазона
    if x!='d':
        try:
            x=list(map(float,(x.split(','))))
        except ValueError:
            print("\nНеверный тип данных\n>",end="")
            while True:
                try:
                    x=input('>')
                    if x=='d':break
                    x=list(map(float,x.split(',')))
                    break
                except ValueError:print("Неверный тип данных",end="")
        points=1
    #Ввод t
    if x=='d':
        x=0
        while True:
            try:
                start=float(input("Введите начало диапазона\n>"))
                break
            except ValueError:print("Неверный тип данных\n>")
        while True:
            try:
                end=float(input("Введите конец диапазона\n>"))
                break
            except ValueError:print("Неверный тип данных.")
        while True:
            try:
                points=int(input("Введите количество элементов\n>"))
                x=np.linspace(start,end,points)
                x=list(map(float,x))
                break
            except (ValueError, TypeError):print("Неверный тип данных или отрицательное значение.")
    
    #Крайние случаи       
    if points==0:
        print("Значения отсутствуют.")
        x=[]
    return x

def greek_alphabet():
    """
    Выводит в консоль греческий алфавит,знак корня и умножения для копипаста.
    """
    print("Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ")
    print("Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω")
    print("α β γ δ ε ζ η θ ι κ λ μ")
    print("ν ξ ο π ρ σ τ υ φ χ ψ ω")
    print("√ ⋅")