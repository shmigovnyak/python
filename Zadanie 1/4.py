ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
cifri ="1234567890"
bukvi = "АБВГДЕЖЗИК"
hod = input().upper()
if(len(hod) == 2 or len(hod) == 3):
    cifri_count = 0
    if (len(hod) == 3):
        if(hod[0] not in bukvi or int(hod[-1]) > 0):
            print("Ход должен быть записан в виде Буква(АБВГДЕЖЗИК):Число(от 1 до 10)")
        else:
            if(hod in ship):
                print("Попал")
            else:
                print("Промах")
    else:
        if(hod[0] not in bukvi or int(hod[-1]) == 0):
            print("Ход должен быть записан в виде Буква(АБВГДЕЖЗИК):Число(от 1 до 10)")
        else:
            if(hod in ship):
                print("Попал")
            else:
                print("Промах")



name = input()
surname = input()
age = input()
print("Ваше имя: {name} , Фамилия: {surname}, Возраст: {age}".format(age=age, name=name, surname=surname))
print(f"Ваше имя: {name} , Фамилия: {surname}, Возраст: {age}")
