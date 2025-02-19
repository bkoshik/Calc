from math import *
import os
from datetime import datetime

date = datetime.now()
hfile = "calc history.txt"

if not os.path.exists(hfile):
    open(hfile, "w").close()

# This vars is first because of errors
lang = "eng"
shure = "n"
con = "y"
num1 = 0
changeLang = "Change language (kz/rus/eng) or to exit enter exit: "
langerror = "Error: Invalid language"

while shure == "n":
    lang = input(changeLang)

    # Variables in english
    if lang == "eng":
        changeLang = "Change language (kz/rus/eng) or to exit enter exit: "
        num1word = "Enter first number: "
        num2word = "Enter second number: "
        opword = "Enter operation (+, -, *, /, ^, sqr, fact, gcd, lcm, sqsum, sqdif): "
        sumword = "Sum: "
        diffword = "Difference: "
        prodword = "Product: "
        quotword = "Quotient: "
        powword = "Power: "
        sqrtword = "Square root: "
        factword = "Factorial: "
        gcdword = "GCD: "
        lcdmword = "LCM: "
        sqsumword = "Square of the sum: "
        sqdifword = "Square of difference: "
        emhistoryword = "History is empty"
        shureword = "Are you sure? (y/n): "
        quesconword = "Ask each time to continue (y/n): "
        conword = "Continue? (y/n): "
        zeroerror = "Error: Division by zero"
        langerror = "Error: Invalid language"
        operror = "Error: Enter correct operation"
    # Variables in russian
    elif lang == "rus":
        changeLang = "Изменить язык (kz/rus/eng) или чтобы выйти введите exit: "
        num1word = "Введите первое число: "
        num2word = "Введите второе число: "
        opword = "Введите операцию (+, -, *, /, ^, sqr, fact, gcd, lcm, sqsum, sqdif): "
        sumword = "Сумма: "
        diffword = "Разность: "
        prodword = "Произведение: "
        quotword = "Частное: "
        powword = "Степень: "
        sqrtword = "Квадратный корень: "
        factword = "Факториал: "
        gcdword = "НОД: "
        lcmword = "НОК: "
        sqsumword = "Квадрат суммы: "
        sqdifword = "Квадрат разности: "
        emhistoryword = "История пуста"
        shureword = "Вы уверены? (y/n): "
        quesconword = "Спрашивать каждый раз продолжить (y/n): "
        conword = "Продолжить? (y/n): "
        zeroerror = "Ошибка: Деление на ноль"
        langerror = "Ошибка: Неверный язык"
        operror = "Ошибка: Введите правильную операцию"
    # Variables in kazakh
    elif lang == "kz":
        changeLang = "Тілді өзгерту (kz/rus/eng) немесе шығу үшін exit жазыңыз: "
        num1word = "Бірінші санды енгізіңіз: "
        num2word = "Екінші санды енгізіңіз: "
        opword = "Операцияны енгізіңіз (+, -, *, /, ^, sqr, fact, gcd, lcm, sqsum, sqdif): "
        sumword = "Қосынды: "
        diffword = "Айырмашылық: "
        prodword = "Көбейту: "
        quotword = "Бөліну: "
        powword = "Дәрежесі: "
        sqrtword = "Квадрат түбірі: "
        factword = "Факториал: "
        gcdword = "ЕҮОБ: "
        lcmword = "ЕКОЕ: "
        sqsumword = "Қосындының квадраты: "
        sqdifword = "Айырмашылық квадраты: "
        emhistoryword = "Тарих бос"
        shureword = "Сіз сенімдісіз бе? (y/n): "
        quesconword = "Әр жолы жалғастыруды сұрау қою керек (y/n): "
        conword = "Жалғастыру? (y/n): "
        zeroerror = "Қате: Нольға бөлу"
        langerror = "Қате: Дұрыс тілді таңдаңыз"
        operror = "Қате: Дұрыс операция енгізіңіз"
    # To exit
    elif lang == "exit":
        exit()
    # If user enters unknown lang
    if lang != "kz" and lang != "rus" and lang != "eng":
        print(langerror)
        continue
    shure = input(shureword)
    quescon = input(quesconword)

# Operations
while con == "y":
    # Op is first because of if/else
    op = input(opword)
    hresult = ""

    if op == "sqr" or op == "fact":
        num1 = float(input(num1word))
    else:
        num1 = float(input(num1word))
        num2 = float(input(num2word))

    match op:
        case "+":
            print(sumword + str(num1 + num2))
            hresult = f"{num1} + {num2} = {num1+num2}"
        case "-":
            print(diffword + str(num1 - num2))
            hresult = f"{num1} - {num2} = {num1-num2}"
        case "*":
            print(prodword + str(num1 * num2))
            hresult = f"{num1} * {num2} = {num1*num2}"
        case "/":
            if num2 == 0:
                print(zeroerror)
                continue
            else:
                print(quotword + str(num1 / num2))
                hresult = f"{num1} / {num2} = {num1/num2}"
        case "^":
            print(powword + str(pow(num1, num2)))
            hresult = f"{num1} ^ {num2} = {pow(num1, num2)}"
        case "sqr":
            print(sqrtword + str(sqrt(num1)))
            hresult = f"√{num1} = {sqrt(num1)}"
        case "fact":
            print(factword + str(factorial(int(num1))))
            hresult = f"{num1}! = {factorial(num1)}"
        case "gcd":
            print(gcdword + str(gcd(int(num1), int(num2))))
            hresult = f"GCD: {num1}, {num2} = {gcd(int(num1), int(num2))}"
        case "lcm":
            print(lcmword + str(lcm(int(num1), int(num2))))
            hresult = f"LCM: {num1}, {num2} = {lcm(int(num1), int(num2))}"
        case "sqsum":
            print(sqsumword + str(num1**2 + 2*num1*num2 + num2**2))
            hresult = f"{num1}^2 + 2*{num1}*{num2} + 2^{num2} = {num1**2 + 2*num1*num2 + num2**2}"
        case "sqdif":
            print(sqdifword + str(num1**2 - 2*num1*num2 + num2**2))
            hresult = f"{num1}^2 - 2*{num1}*{num2} + 2^{num2} = {num1**2 - 2*num1*num2 + num2**2}"
        case "history" | "hst":
            with open(hfile, "r") as file:
                history = file.read()
            print(history if history else emhistoryword)
        case _:
            print(operror)
            continue

    with open(hfile, "a") as file:
        date_str = f"{date.day:02}.{date.month:02}.{date.year}"
        new_entry = f"\t{hresult}\n"

        if os.path.exists(hfile):
            with open(hfile, "r", encoding="utf-8") as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if line.strip() == date_str + ":":
                    lines.insert(i + 1, new_entry)
                    break
            else:
                lines.append(f"{date_str}:\n{new_entry}")
        else:
            lines = [f"{date_str}:\n{new_entry}"]

        # Записываем обновленные данные обратно в файл
        with open(hfile, "w", encoding="utf-8") as file:
            file.writelines(lines)
    
    # To ask user
    if quescon == "y":
        con = input(conword)