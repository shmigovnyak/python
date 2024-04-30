slovo = input("Введите слово ")
bukva = input("Введите символ ")
count = 0
for i in slovo:
    if i == bukva:
        count += 1
slovar = {bukva: count}
print(slovar)