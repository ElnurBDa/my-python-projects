z = 0
r = 0
b = 0
for x in range(10, 1000000):
    b = x
    while x != 1.0:
        if x % 2 == 0:
            x = x / 2
            z += 1

        if x % 2 == 1 and x != 1:
            x = 3 * x + 1
            z += 1

        a = z
    if max(r, a) == a:
        r = a
        print("____")
        print(b, "|", r)
        print("___")
    z = 0
# 837799 is answer
