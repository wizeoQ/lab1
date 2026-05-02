import formatter as f


def run_exercise_7() -> None:
    """
    Выполняет упражнения 7.
    """
    f.ex(7)
    f.l()
    array = f.multi_input()
    if len(array) == 0:
        return
    print(array)
    f.l()
    sorted_array = sorted(array)
    print(sorted_array)
