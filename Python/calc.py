def calculation(a,b):
    o = input("Введите тип операции(+-*/):")
    while o not in "+-*/":
        o = input(f"Некорректный тип операции: {o} \nВведите тип операции(+-*/):")
    if o == "+":
        print(f"Результат сложения {a} и {b} = {a + b}")
    elif o == "-":
        print(f"Результат вычитания {b} из {a} = {a - b}")
    elif o == "*":
        print(f"Результат умножения {a} на {b} = {a * b}")
    elif o == "/":
        try:
            print(f"Результат деления {a} на {b} = {a / b}")
        except ZeroDivisionError:
            print(f"На 0 делить нельзя!")

def is_number():
    a = input("Введите первое число: ")
    while not a.isnumeric():
        print(f"Введенный символ {a} не является числовым\n")
        a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    while not b.isnumeric():
        print(f"Введенный символ {b} не является числовым\n")
        b = input("Введите второе число: ")
    calculation(int(a),int(b))
is_number()