import re

phone_number = input("Введите номер телефона: ")
def check_phone_number(phone_number):


    if len(re.sub(r'\D', '', phone_number)) < 11:
        print("Неверный номер телефона.")
        return


    pattern = r"^((\+7|7|8)-?)?(\d{3}-?\d{3}-?\d{2}-?\d{2})$"
    if re.match(pattern, phone_number):
        print("Номер телефона верный.")
    else:
        print("Неверный номер телефона.")



check_phone_number(phone_number)