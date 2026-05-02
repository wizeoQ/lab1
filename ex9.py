import formatter as f


def run_exercise_9(variant: int=1) -> None:
    """
    Выполняет упражнение 9.
    
    У этого упражнения есть 12 вариантов заданий:
    1, 2, 3, ... , 11, 12
    По умолчанию выполняется вариант 1.
    """
    f.ex(9)
    f.l()
    if variant == 1:
        count = 0
        text = "Етижи-пассатижи едрид его рыстудыть,\
        лететь, блин!Еее??Елека есенин"
        print(text)
        f.l()
        text_process = text.lower()
        text_process = text_process.replace("?", " ")
        text_process = text_process.replace("!", " ")
        text_process = text_process.replace(".", " ")
        text_process = text_process.replace(",", " ")
        text_separate = text_process.split()
        for word in text_separate:
            while True:
                if word[0] == "е":
                    count += 1
                    break
                else: break
        print("Количество слов на \"Е\" - ", count)

    elif variant == 2:
        text = "Этот знак \":\": нужен чтобы ставить : с помощью: :"
        print(text)
        f.l()
        text_replace = text.replace(":", "%")
        count = text_replace.count("%")
        print(text_replace)
        print("Количество замен - ", count)

    elif variant == 3:
        count = 0
        text = "Система - гарант порядка. Порядок - высший приоритет.\
        Приоритеты - основа системы. Система - гарант порядка..."
        print(text)
        f.l()
        for i in text:
            if i == ".":
                count += 1
        text_without_dots = text.replace(".","")
        print(text_without_dots)
        print("Количество удалений - ", count)

    elif variant == 4:
        pred_count = 0
        post_count = 0
        text = "Агитация агентов огромной академии"
        print(text)
        f.l()
        for i in text:
            if i == "о" or i == "О":
                pred_count += 1
        text_replace = (text.replace("а", "о")).replace("А", "О")
        for i in text_replace:
            if i == "о" or i == "О":
                post_count += 1
        count = post_count - pred_count
        print(text_replace)
        print("Количество замен - ", count)

    elif variant == 5:
        text = "Система - гарант порядка."
        print(text)
        text_upper = text.upper()
        print(text_upper)

    elif variant == 6:
        count = 0
        text = "Система - гарант порядка. Порядок - высший приоритет.\
        Приоритеты - основа системы. Система - гарант порядка..."
        print(text)
        f.l()
        for i in text:
            if i == "а" or i == "А":
                count += 1
        text_without_A = (text.replace("А", "")).replace("а", "")
        print(text_without_A)
        print("Количество удалений - ", count)

    elif variant == 7:
        text = "Продуктивность - первый приоритет. Вперёд к победе."    
        pred=list(text)
        i=0
        temp=''
        while i!=(int(len(pred)/2)):
            if (pred[i]=="П" or pred[i]=="п"):
                pred[i]='*'
            i+=1
        for i in pred:
            temp=temp+i
        print(temp)

    elif variant == 8:
        text = "Система? Гарант! Порядок. Порядок - высший приоритет."
        print(text)
        f.l()
        text_process = text.lower()
        text_process = text_process.replace("?", " ")
        text_process = text_process.replace("!", " ")
        text_process = text_process.replace(".", " ")
        text_process = text_process.replace(",", " ")
        text_process = text_process.replace(" -", " ")
        text_process = text_process.replace("- ", " ")
        text_separate = text_process.split()
        print(text_separate)
        print("Количество слов в строке - ", len(text_separate))

    elif variant == 9:
        text = "Ехал Грека через реку - видит Грека в реке рак.\
        сунул Грека в реку руку - Греку в реке руку цап."
        print(text)
        count = text.count("Грека")
        f.l()
        print("Количество слов \"Грека\" - ", count)

    elif variant == 10:
        text_final = ""
        text = "The system is the guarantor of order."
        print(text)
        text_separate = text.split()
        for i in text_separate:
            i = i.capitalize()
            text_final = text_final+i+" "
        f.l()
        print(text_final)

    elif variant == 11:
        text = "Народное! длинное! направление! ноющих! недотёп! - НННН!!!"
        print(text)
        f.l()
        text_lower = text.lower()
        if text_lower.find("н") != -1:
            count = 1
            while True:
                if text_lower.find("н" * (count + 1)) != -1:
                    count += 1
                else: break
            print ("Максимальное количество \"Н\" идущих подряд -", count)
        else: print("\"Н\" отсутствует в строке.")
        f.l()
        text_with_points = text.replace("!",".")
        print(text_with_points)

    elif variant == 12:
        count = 0
        text = "Не легка доля наша, но и соразмерна будет награда."
        print(text)
        f.l()
        text_process = text.lower()
        text_process = text_process.replace("?", " ")
        text_process = text_process.replace("!", " ")
        text_process = text_process.replace(".", " ")
        text_process = text_process.replace(",", " ")
        text_process = text_process.replace(" -", " ")
        text_process = text_process.replace("- ", " ")
        text_separate = text_process.split()
        for word in text_separate:
            if word[-1] == "а":
                count +=1
        print("Количество слов, кончающихся на \"а\" - ", count)

    else:
        print("Вариант, указанный в аргументе отсутствует.")
