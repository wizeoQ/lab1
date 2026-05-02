import numpy as np
import matplotlib.pyplot as plt
import wizeo_lib as f


def run_exercise_2() -> None:
    """
    Выполняет упражнение №2
    """
    f.ex(2)
    #-------------Вывод формулы--------------
    print("\n      9*πt+10cos(x)")
    print("Z = ──────────────── * e^x")
    print("      √(t)-|sin(t)|")
    f.l()
    #-------------Ввод данных----------------    
    print("Введите x", end="")
    x = f.defend_input()
    f.l()
    print("Введите t")
    t = f.multi_input()
    if len(t) == 0: return
    #------------------Блок вычислений----------------
    z = []
    for i in t:
            if i == 0:
                z.append(np.nan)
            else: 
                numerator = 9 * np.pi * i + 10 * np.cos(x)
                denominator = np.sqrt(complex(i)) - abs(np.sin(i))
                answer = numerator / denominator * np.exp(x)
                z.append(answer)
    #-----------------Печать и график-----------------
    def print_z():
        f.l()
        for i, j in zip(t, z):
            print("Z(", round(i, 3), ")", sep="", end="")
            print(" = ", f.simple_complex(j, 3), sep="")
    
    
    def graph():
        if len(z) > 30:
            plt.plot(t, np.real(z), '-r')
            plt.plot(t, np.imag(z), '-g')
        else:
            plt.plot(t, np.real(z), '-or')
            plt.plot(t, np.imag(z), '-og')
        f.l()
        plt.legend(['Re(Z)', 'Im(Z)'])
        plt.title("Зависимость Z от t")
        plt.xlabel("t")
        plt.ylabel("Z(t)")
        plt.grid()
        plt.show()
    #----------------Интерфейс-------------------------
    f.l()
    print("Вывести рассчитанные значения?")
    print("Предупреждение: Их может быть много.")
    f.yes_or_not(print_z)
    f.l()
    print("Нужен ли вывод графика?")
    f.yes_or_not(graph)    
