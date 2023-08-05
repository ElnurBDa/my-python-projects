'''Calculator_v3'''
'''+|-|*|/|^|sin|cos|tan|cot'''
'''new function for calculator_v3 is that  you can exit'''
import tool_for_calculator_v3
from colorama import init
from colorama import Fore, Back, Style
import math
init()
print(Fore.GREEN)
print("Calculator v3")
a=0
popItok = 100
d = ""
while a < math.inf and d != "exit" :
    try:
        print(Fore.LIGHTBLUE_EX)
        x=float(input("x="))
        y=float(input("y="))
        print(Fore.LIGHTMAGENTA_EX)
        operation= input("What operation you need?(+|-|*|/|^|trigonometry)")
        if operation == "+":
            tool_for_calculator_v3.addition(x, y)
        elif operation == "-":
            tool_for_calculator_v3.subtraction(x, y)
        elif operation == "*":
            tool_for_calculator_v3.multiplication(x, y)
        elif operation == "/":
            tool_for_calculator_v3.division(x, y)
        elif operation == "^":
            tool_for_calculator_v3.exponentiation(x, y)
        elif operation == "trigonometry":
            tool_for_calculator_v3.trigonometry_sin_cos_tan_cot(x, y)
        else:
            print(Fore.RED)
            print("                   Unknown opertion.")
    except :
        print(Fore.RED)
        print("Error!")
    print(Fore.GREEN)
    d = input("If you want to exit , print \"exit\" .If you don't want to exit press\"Enter\"")
    a = a+1
print(Fore.GREEN)
print("The man who create it is Elnur.")
input("Thanks for using!")




