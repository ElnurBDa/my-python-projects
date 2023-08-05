#решено
a, b = 0, 0
for x in range(1, 101):
    a = a + x * x
    b = b + x
print(b * b - a)
# 25164150
