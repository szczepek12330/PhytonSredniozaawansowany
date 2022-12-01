wybor = int(input("""wybierz rodzaj działania 1-mnożenie,2-dzielenie,3-dodawanie,4-odejmowanie

"""))

if (wybor > 5):

    print("Wybrano złe działanie")

elif (wybor < 1):

    print("Wybrano złe działanie")

else:

    print("Podaj pierwszą liczbe")

    a_liczba = float(input())

    print("Podaj druga liczbe")

    b_liczba = float(input())

    if (wybor == 1):

        print(a_liczba * b_liczba)

    elif (wybor == 2):

        if (a_liczba == 0):

            print("Nie dziel przez zero")

        elif (b_liczba == 0):

            print("Nie dziel przez zero")

        else:

            print(a_liczba / b_liczba)

    elif (wybor == 3):

        print(a_liczba + b_liczba)

    elif (wybor == 4):

        print(a_liczba - b_liczba)