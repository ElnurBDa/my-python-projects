#какие корни из числа не возможно нарисовать на бумагу
def is_representable(n):
    # a и b квадраты каких то чисел
    spisok = []
    for a in range(1, n + 1):
        for b in range(0, n - a + 1):
            c = n - b - a
            if (b ** .5).is_integer() and (a ** .5).is_integer() and (c ** .5).is_integer() and sorted(
                    (a ** .5, b ** .5, c ** .5)) not in spisok:
                spisok.append(sorted((a ** .5, b ** .5, c ** .5)))
    return spisok

count=0
for x in range(1, 1001):
    if len(is_representable(x))==0:
        print(x)
        count+=1
print(count)
