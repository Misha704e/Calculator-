while True:
        num1 = int(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /): ")
        num2 = int(input("Введіть друге число: "))
        if operator == "+":
            result = num1 + num2
            print(result)
        elif operator == "-":
            result = num1 - num2
            print(result)
        elif operator == "*":
            result = num1 * num2
            print(result)
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
                print(result)
            else:
                print("Ділення на нуль неможливе!")
                continue
        else:
            print("Невірний оператор!")
            continue
            ###
        choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
        if choice != "так":
            print("До побачення!")
            break