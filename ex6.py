import numpy as np
from numpy import nan, pi, cos, sin, log, exp, sqrt
import matplotlib.pyplot as plt
import formatter as f


def run_exercise_6() -> None:
    """
    Выполняет упражнение №6"
    """
    f.ex(6)
    # Вывод формулы
    print("\n           / α⋅[(5πt)^2 + 3cos(2x)]\\")
    print("Z(t,x,α) = |────────────────────────| ⋅ β")
    print("           \\  ln(|t|+1) - sin(t)^2 /")
    print("\n, где β = e^(-αx) + √αt")
    f.l()
    # Ввод t
    print("Введите t")
    t = f.multi_input()
    # Крайние случаи       
    if len(t) == 1 and t[0] == 0:
        print("Деление на ноль.")
        return
    if len(t) == 0:
        return
    #Ввод x и a
    f.l()
    print("Введите X", end="")
    x = f.defend_input()
    f.l()
    print("Введите α", end="")
    while True:
        a = f.defend_input()
        if 0.1 <= a <= 5: break
        else: print("Значения нет в диапазоне.", end="")
    f.l()
    #Расчёт Z
    z = []
    for t_i in t:
        if t_i == 0: z.append(nan)
        else:
            nmrtr = a * ((5 * pi * (t_i ** 2)) + 3 * cos(2 * x))
            dnmtr = log(abs(t_i) + 1) - sin(t_i) ** 2
            answ = nmrtr / dnmtr * exp(-a * x) + sqrt(complex(a * t_i))
            z.append(answ)
    # Вывод данных.
    def out_z():
        f.l()
        print("Z(t, x, α) = ...")
        x_out = f.simple_complex(x, 3, 0)
        a_out = f.simple_complex(a, 3, 0)
        for t_i, z_i in zip(t, z):
            t_out = f.simple_complex(t_i, 3, 0)
            z_out = f.simple_complex(z_i, 3, 0)
            print("Z(", t_out, ", ", x_out, sep="", end="")
            print(", ", a_out, ") = ", z_out, sep="") 
    # Построение графика
    def graph():
        if len(z) > 30:
            plt.plot(t, np.real(z), '-r')
            plt.plot(t, np.imag(z), '-g')
        else:
            plt.plot(t, np.real(z), '-or')
            plt.plot(t, np.imag(z), '-og')
        plt.xlabel("t")
        plt.ylabel("Z(t)")
        plt.title("Зависимость Z от t")
        plt.legend(["Re(Z)", "Im(Z)"])
        plt.show()
    # Интерфейс
    print("Вывести данные?")
    f.yes_or_not(out_z)
    f.l()
    print("Вывести график?")
    f.yes_or_not(graph)
