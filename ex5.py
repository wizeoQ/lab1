import formatter as f


def run_exercise_5() -> None:
    """
    Выполняет упражнение 5
    """
    f.ex(5)
    string = input("Это палиндром?\n>")
    string = string.lower()
    if string == "": print("Да")
    else:
        i = 0
        while i != len(string):
            if string[i] != string[-i - 1]:
                print("Нет")
                break
            if i == len(string) // 2:
                print("Да")
                break
            i += 1
