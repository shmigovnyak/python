import re
import calendar

def calendarr():

    while True:
        year_month = input("Введите дату в формате 'ГГГГ-ММ': ")
        if re.match(r"\d{4}-\d{2}", year_month):
            break
        else:
            print("Неверный формат даты. Используйте формат 'ГГГГ-ММ'.")


    year, month = map(int, year_month.split('-'))


    if year < 0 or month < 1 or month > 12:
        return "Некорректные значения для года или месяца."


    return calendar.month(year, month)



print(calendarr())

