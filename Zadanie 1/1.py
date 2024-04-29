while(True):
    chislo = input('Введите число: ')
    try:
        if (chislo == "exit"):
            break
        length = int(chislo)
        print(len(chislo))
    except ValueError:
        print("Ошибка! Несоответствие типа данных")
        break



