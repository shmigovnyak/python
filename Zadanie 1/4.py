ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
hod = input().upper()
if (hod in ship):
    print("Есть пробитие")
else:
    print("МАЗИЛА")

name = input()
surname = input()
age = input()
print("Ваше имя: {name} , Фамилия: {surname}, Возраст: {age}".format(age=age, name=name, surname=surname))
print(f"Ваше имя: {name} , Фамилия: {surname}, Возраст: {age}")
