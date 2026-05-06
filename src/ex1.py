import wizeo_lib as f


def run_exercise_1() -> None:
    """
    Выполняет упражнение №1
    """
    f.ex(1)
    print("Ваши имя, фамилия, отчество?", end="")
    # Ввод имени
    allowed = f.alphabet() + " -()'"
    while True:
        name = input("> ")
        if name == "":
            print("ОТДАЙ ДАННЫЕ.", end="")
        elif not all(i in allowed for i in name):
            print("Ваши НОРМАЛЬНЫЕ имя, фамилия, отчество?", end="") 
        else:
            break
    # Ввод возраста
    f.l()
    print("Сколько Вам лет?", end="")
    while True:
        age = 0
        try:
            age = input("> ")
            if age == "":
                print("ОТДАЙ ДАННЫЕ.", end="")
                continue
            age = float(age)
            if float(age) != int(age):
                raise ValueError
            age = int(age)
            if age < 0:
                print("Родись, а потом поговорим.")
                return
            elif age > 100:
                print("Хиппуешь, плесень?")
                return
            else:
                break
        except ValueError:
            try:
                if float(age) != int(age):
                    print("Будь проще.", end="")
            except ValueError:
                print("Возраст - это всего лишь цифра.", end="")
    # Ввод города
    f.l()
    print("Где вы живёте?", end="")
    while True:
        place = input("> ")
        if place == "":
            print("ОТДАЙ ДАННЫЕ.", end="")
        else:
            break
    # Вывод данных
    f.l()
    print("Ваши ФИО -", name)
    print("Ваш возраст -", age)
    print("Ваше место жительство -", place)
