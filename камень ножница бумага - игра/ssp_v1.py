# ssp_v1


import random
from colorama import init
from colorama import Fore, Style

init()
print(Fore.GREEN)
print("---Game---")
print(Fore.CYAN)
print("Камень/Ножница/Бумага")
t = 1
pobeda = 0
nichya = 0
porajeniye = 0
errors = 0
while t < 11:
    app = random.randint(1, 3)
    if app == 1:
        e = "Камень"
    elif app == 2:
        e = "Ножницы"
    else:
        e = "Бумага"
    print(Fore.MAGENTA)
    print("Раунд " + str(t))
    print(Fore.GREEN)
    print("1)Камень")
    print("2)Ножницы")
    print("3)Бумага")

    try:
        print(Fore.LIGHTGREEN_EX)
        x = int(input("Выбери номер \n> "))
        if x == 1:
            print(Fore.GREEN)
            print("")
            print("Ты выбрал камень.")
            print("А компуктер выбарал " + str(e))
            print("")
            if app == 1:
                print(Fore.BLUE)
                print("Ничья.")
                nichya = nichya + 1
            elif app == 2:
                print(Fore.LIGHTCYAN_EX)
                print("Ты победил!")
                pobeda = pobeda + 1
            else:
                print(Fore.LIGHTRED_EX)
                print("Победил компуктер.\nТы проиграл.")
                porajeniye = porajeniye + 1
            print("")
        elif x == 2:
            print(Fore.GREEN)
            print("")
            print("Ты выбрал ножницы.")
            print("А компуктер выбарал " + str(e))
            print("")
            if app == 1:
                print(Fore.LIGHTRED_EX)
                print("Победил компуктер.\nТы проиграл.")
                porajeniye = porajeniye + 1
            elif app == 2:
                print(Fore.BLUE)
                print("Ничья.")
                nichya = nichya + 1
            else:
                print(Fore.LIGHTCYAN_EX)
                print("Ты победил!")
                pobeda = pobeda + 1
            print("")
        elif x == 3:
            print(Fore.GREEN)
            print("")
            print("Ты выбрал бумагу.")
            print("А компуктер выбарал " + str(e))
            print("")
            if app == 1:
                print(Fore.LIGHTCYAN_EX)
                print("Ты победил!")
                pobeda = pobeda + 1
            elif app == 2:
                print(Fore.LIGHTRED_EX)
                print("Победил компуктер.\nТы проиграл.")
                porajeniye = porajeniye + 1
            else:
                print(Fore.BLUE)
                print("Ничья.")
                nichya = nichya + 1
            print("")
        else:
            print(Fore.RED)
            print("Пиши только те числа(1,2,3) !")
            errors = errors + 1
    except:
        print(Fore.RED)
        print("Пиши только эти числа(1,2,3) ! ")
        errors = errors + 1
    t = t + 1
print(Fore.LIGHTYELLOW_EX)
print("Побед : " + str(pobeda))
print("Ничья : " + str(nichya))
print("Поражений : " + str(porajeniye))
if errors > 0:
    print(Fore.RED)
    print("Ошибок : " + str(errors))
print(Style.RESET_ALL)
print("The man who create it is Elnur.")
print("Thanks for using!\nк_н_б_v1")
input("Press \"Enter\" for exit.")
