
from typing import List, Union

def function(elements: List[Union[int, float]], chislo: Union[int, float] = 2) -> List[Union[int, float]]:
    return [element * chislo for element in elements]

function_lambda = lambda elements, chislo=2: [element * chislo for element in elements]

def run_program():
    while True:
        elements_input = input("Введите элементы списка через пробел: ")
        elements = [float(element) for element in elements_input.split()]
        if elements_input == "стоп":
            print("Программа завершена")
            break


        chislo_input = input("Введите число для умножения (если ничего не введете, умножит на 2): ")
        if chislo_input:
            chislo = float(chislo_input)
        else:
            chislo = 2

        result_function = function(elements, chislo)
        result_lambda = function_lambda(elements, chislo)

        print("Результат с использованием функции:", result_function)
        print("Результат с использованием лямбда-функции:", result_lambda)
        again = input("Хотите выполнить еще одну операцию? (да/нет): ")
        if again.lower() != 'да':
            print("Программа завершена.")
            break

run_program()