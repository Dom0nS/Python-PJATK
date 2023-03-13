if __name__ == '__main__':
    print("Witaj w kalkulatorze!")

    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    print("\nWybierz operator, który chcesz wykonać:")
    print("+ - Dodawanie")
    print("- - Odejmowanie")
    print("* - Mnożenie")
    print("/ - Dzielenie")
    print("// - Dzielenie całkowite")
    print("% - Dzielenie z resztą")
    print("** - Potęgowanie")

    operator = input("Twój wybór (+/-/*/ ////%/**): ")

    if operator == "+":
        wynik = a + b
        znak = "+"
    elif operator == "-":
        wynik = a - b
        znak = "-"
    elif operator == "*":
        wynik = a * b
        znak = "*"
    elif operator == "/":
        if b == 0:
            print("Nie można dzielić przez 0!")
        else:
            wynik = a / b
            znak = "/"
    elif operator == "//":
        if b == 0:
            print("Nie można dzielić przez 0!")
        else:
            wynik = a // b
            znak = "//"
    elif operator == "%":
        if b == 0:
            print("Nie można dzielić przez 0!")
        else:
            wynik = a % b
            znak = "%"
    elif operator == "**":
        wynik = a ** b
        znak = "**"
    else:
        print("Nieznany operator")

    if "wynik" in locals():
        print(f"\n{a} {znak} {b} = {wynik}")
