'''tool for calculator v3'''
import math
def addition(x, y):
    result = x + y
    print("Result = " + str(result))
def subtraction(x, y):
    result = x - y
    print("Result = " + str(result))
def division(x, y):
    result = x / y
    print("Result = " + str(result))
def multiplication(x, y):
    result = x * y
    print("Result = " + str(result))
def exponentiation(x, y):
    print("(x^y)")
    result = pow(x, y)
    print("Result = " + str(result))
def trigonometry_sin_cos_tan_cot(x, y):
    print("sin(x)              cos(x)             tan(x)             cot(x)             sin(y)             cos(y)             tan(y)             cot(y)")
    result1 = math.sin(x)
    result2 = math.cos(x)
    result3 = math.tan(x)
    result7 = result2 / result1
    result4 = math.sin(y)
    result5 = math.cos(y)
    result6 = math.tan(y)
    result8 = result5 / result4
    print(str(result1) +"|"+ str(result2) +"|"+ str(result3) +"|"+ str(result7) + "|"+str(result4) +"|"+ str(result5) +"|"+ str(result6)+"|"+ str(result8))


