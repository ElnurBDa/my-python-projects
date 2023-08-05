#проверка для произведений двухзначный чисел
a = [
    9,8,7,6,5,4,3,2,1,0
]
b = [
    9,8,7,6,5,4,3,2,1,0
]
e = 100
r = 100
for x in a:
    for y in b:
        while e >9:
            e = e - 1
            while r >9:
                if e * r == x * 1001 + y * 110 and e*r >9000:
                    print("_______")
                    print(e)
                    print(r)
                    print(e * r)
                r = r - 1
            r = 100
        e=100