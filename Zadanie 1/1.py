while(True):
    try:
        chislo = input()
        if (chislo == "exit"):
            break
        print(len(chislo))
    except ValueError:
        print("Ошибка! Несоответствие типа данных")
        break