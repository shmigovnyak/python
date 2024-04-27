from itertools import permutations
chislo = input()
try:
    cifri = []
    for i in chislo:
        cifri.append(int(i))
    print(list(permutations(cifri)))
    if(len(set(cifri)) != len(cifri)):
        print("Есть повторяющиеся цифры")
except ValueError:
        print("Введите трёхзначное число")

