def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Входные данные должны быть числами")

def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход из программы")

        choice = input("Введите номер операции: ")

        if choice == '6':
            print("Программа завершена.")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 6.")
            continue

        try:
            numbers = [float(num) for num in input("Введите числа через пробел: ").split()]
            validate_input(numbers)
        except ValueError as e:
            print("Ошибка:", e)
            continue

        if choice == '1':
            print("Результат:", sum(numbers))
        elif choice == '2':
            print("Результат:", numbers[0] - sum(numbers[1:]))
        elif choice == '3':
            print("Результат:", eval('*'.join(map(str, numbers))))
        elif choice == '4':
            try:
                print("Результат:", eval('/'.join(map(str, numbers))))
            except ZeroDivisionError:
                print("Ошибка: Делить на 0 нельзя")
        elif choice == '5':
            print("Результат:", eval('**'.join(map(str, numbers))))

calculator()
