import random as rnd
import formatter as f


def run_exercise_4() -> None:
    """
    Выполняет задание №4
    """
    f.ex(4.1)
    price = float(rnd.randint(50, 1000))
    if price % 100 == 0: 
        price -= 0.01
    for i in range(1, 11):
        print(i, " кг конфет - ", round(i * price, 2), " рублей.", sep="")
   
    f.ex(4.2)
    sequance = []
    for i in [''] * rnd.randint(5, 20):
        sequance.append(rnd.randint(1, 100))
    sequance.append(0)
    i, sum_sq = 0, 0
    print(sequance)
    while  i != len(sequance):
        sum_sq = sum_sq + sequance[i]
        i += 1
    print("Сумма чисел -", sum_sq)
    print("Количество чисел -", len(sequance))
