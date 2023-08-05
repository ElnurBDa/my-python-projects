'''Calculator_v1'''
'''+ - * / ^ sin cos tan !'''
from colorama import init
from colorama import Fore, Back, Style
import math

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
init()
print("Calculator_v2")
try:
    print(Fore.LIGHTCYAN_EX)
    n1 = float(input("(1): "))
    n2 = float(input("(2): "))
    print(Fore.LIGHTMAGENTA_EX)
    op = input("Operation(+ , - , * , / , ^ , sin , cos , tan , !): ")
    print(Fore.LIGHTYELLOW_EX)
    if op == "+":
        result = n1 + n2
        print("(1)+(2)= " + str(result))
    elif op == "-":
        result = n1 - n2
        print("(1)-(2)= " + str(result))
    elif op == "/":
        result = n1 / n2
        print("(1)/(2)= " + str(result))
    elif op == "*":
        result = n1 * n2
        print("(1)*(2)= " + str(result))
    elif op == "^":
        result = n1 ** n2
        print("(1)^(2)= " + str(result))
    elif op == "sin":
        result1 = math.sin(n1)
        result2 = math.sin(n2)
        print("sin(1) = " + str(result1) + "\nsin(2) = " + str(result2))
    elif op == "cos":
        result1 = math.cos(n1)
        result2 = math.cos(n2)
        print("cos(1) = " + str(result1) + "\ncos(2) = " + str(result2))
    elif op == "tan":
        result1 = math.tan(n1)
        result2 = math.tan(n2)
        print("tan(1) = " + str(result1) + "\ntan(2) = " + str(result2))
    elif op == "!":
        result1 = math.factorial(n1)
        result2 = math.factorial(n2)
        print("(1)! = " + str(result1) + "\n(2)! = " + str(result2))
    else:
        print(Fore.RED)
        print("Unknown opertion")
except:
    print(Fore.RED)
    print("Error")
print(Style.RESET_ALL)
print("The man who create it is Elnur.")
print("Thanks for using!")
input("Press \"Enter\" for exit.")
