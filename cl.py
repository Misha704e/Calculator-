while True:
        n1 = int(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /): ")
        n2 = int(input("Введіть друге число: "))
        if operator == "+":
            result = n1 + n2
            print(result)
        elif operator == "-":
            result = n1 - n2
            print(result)
        elif operator == "*":
            result = n1 * n2
            print(result)
        elif operator == "/":
            if num2 != 0:
                result = n1 / n2
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
