a = input("Введите число, в котором все цифры различны:")
d = []
if len(a)!=3:
    print('Число не трехзначное')
else:
    for i in a:
        d.append(int(i))
    if(len(set(d)) != len(d)):
        print("Есть повторяющиеся цифры")
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    if(i != j & j != k & k != i):
                        print(d[i], d[j], d[k])
