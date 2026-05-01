import formatter as f

variant = 1
f.eq(9)
if variant == 1:
    count = 0
    text = "Етижи-пассатижи едрид его рыстудыть, лететь, блин!Еее??Елека есенин"
    print(text)
    f.l()
    text_process = text.lower()
    text_process = text.replace("?", " ")
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