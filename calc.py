from math import *

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
        opword = "Enter operation (+, -, *, /, ^, sqr, fact, gcd, lcm): "
        sumword = "Sum: "
        diffword = "Difference: "
        prodword = "Product: "
        quotword = "Quotient: "
        powword = "Power: "
        sqrtword = "Square root: "
        factword = "Factorial: "
        gcdword = "GCD: "
        lcdmword = "LCM: "
        shureword = "Are you sure? (y/n): "
        conword = "Continue? (y/n): "
        zeroerror = "Error: Division by zero"
        langerror = "Error: Invalid language"
        operror = "Error: Enter correct operation"
    # Variables in russian
    elif lang == "rus":
        changeLang = "Изменить язык (kz/rus/eng) или чтобы выйти введите exit: "
        num1word = "Введите первое число: "
        num2word = "Введите второе число: "
        opword = "Введите операцию (+, -, *, /, ^, sqr, fact, gcd, lcm): "
        sumword = "Сумма: "
        diffword = "Разность: "
        prodword = "Произведение: "
        quotword = "Частное: "
        powword = "Степень: "
        sqrtword = "Квадратный корень: "
        factword = "Факториал: "
        gcdword = "НОД: "
        lcmword = "НОК: "
        shureword = "Вы уверены? (y/n): "
        conword = "Продолжить? (y/n): "
        zeroerror = "Ошибка: Деление на ноль"
        langerror = "Ошибка: Неверный язык"
        operror = "Ошибка: Введите правильную операцию"
    # Variables in kazakh
    elif lang == "kz":
        changeLang = "Тілді өзгерту (kz/rus/eng) немесе шығу үшін exit жазыңыз: "
        num1word = "Бірінші санды енгізіңіз: "
        num2word = "Екінші санды енгізіңіз: "
        opword = "Операцияны енгізіңіз (+, -, *, /, ^, sqr, fact, gcd, lcm): "
        sumword = "Қосынды: "
        diffword = "Айырмашылық: "
        prodword = "Көбейту: "
        quotword = "Бөліну: "
        powword = "Дәрежесі: "
        sqrtword = "Квадрат түбірі: "
        factword = "Факториал: "
        gcdword = "ЕҮОБ: "
        lcmword = "ЕКОЕ: "
        shureword = "Сіз сенімдісіз бе? (y/n): "
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

# Operations
while con == "y":
    # Op is first because of if/else
    op = input(opword)
    if op == "sqr" or op == "fact":
        num1 = float(input(num1word))
    else:
        num1 = float(input(num1word))
        num2 = float(input(num2word))

    match op:
        case "+":
            print(sumword + str(num1 + num2))
        case "-":
            print(diffword + str(num1 - num2))
        case "*":
            print(prodword + str(num1 * num2))
        case "/":
            if num2 == 0:
                print(zeroerror)
                continue
            else:
                print(quotword + str(num1 / num2))
        case "^":
            print(powword + str(pow(num1, num2)))
        case "sqr":
            print(sqrtword + str(sqrt(num1)))
        case "fact":
            print(factword + str(factorial(int(num1))))
        case "gcd":
            print(gcdword + str(gcd(int(num1), int(num2))))
        case "lcm":
            print(lcmword + str(lcm(int(num1), int(num2))))
        case _:
            print(operror)
            continue
    
    # To ask user
    con = input(conword)


# In plans create calc on C++