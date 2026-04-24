import formatter as f

def run_exercise_1():
    f.ex(1)
    
    name = input ("Ваши имя, фамилия, отчество?\n\t> ")
    age = input ("Сколько Вам лет?\n\t> ")
    place = input ("Где Вы живёте?\n\t> ")
    
    f.d(3)
    
    print("Ваши ФИО -", name, end="\n")
    print("Ваш возраст -", age, end="\n")
    print("Вы живёте в -", place, end="")