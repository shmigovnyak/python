def fileWrite(text, filename):
    with open(filename, mode="a+") as file:
        file.write(text + "\n")

def fileRead(filename):
    with open(filename, mode="r") as file:
        for index, line in enumerate(file.readlines()):
            if index % 2 == 1:
                print(line.strip())

filename = "example.txt"
fileWrite("Пример текста для записи в файл 1", filename)
fileWrite("Пример текста для записи в файл 2", filename)
fileWrite("Пример текста для записи в файл 3", filename)
fileWrite("Пример текста для записи в файл 4", filename)
fileRead(filename)

