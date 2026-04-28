import formatter as f

def run_exercise_5():
    f.ex(5)
    string = input("Это палиндром?\n>")
    if string=='':print("Да")
    else:
        i=0
        while i!=len(string):
            if string[i]!=string[-i-1]:
                print("Нет")
                break
            if i==len(string)//2:
                print("Да")
                break
            i+=1