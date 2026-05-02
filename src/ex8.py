import random as rnd
import wizeo_lib as f


def run_exercise_8() -> None:
    """
    Выполняет упражнение 8
    """
    f.ex(8)
    # Формирование массива с случайной длинной и случайными числами
    lenght = rnd.randint(10, 20)
    array = []
    i = 0
    while i != lenght:
        array.append(rnd.randint(10, 99))
        i += 1
    # Собственно, само задание.
    f.l()
    temp = 0
    print("Элемент - Сумма с предыдущим")
    for i in array:
        temp = temp + i
        print(i, " - ", temp)
