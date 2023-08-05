#решено
import math as m
x = 2520 * 11 * 13 * 17 * 19 * 2
a = 0
while a < 21:
    a = a + 1

    if m.fmod(x, a) == 0.0:
        print(a)
print(x)
# Ответ : 232792560
