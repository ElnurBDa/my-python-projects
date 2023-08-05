from math import factorial
from time import time
start = time()
def nck(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
a=20
print('Number of lattice paths is: ' + str(nck(a+a,a)))
end = time()
print(end - start)
input()
