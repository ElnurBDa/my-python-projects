# решено
a, b, c, a_, b_, c_ = 1, 1, 1, 1, 1, 1
while a < 1000:
    while b < 1000:
        while c < 1000:
            if a + b + c == 1000 and c * c == a * a + b * b:
                a_ = a
                b_ = b
                c_ = c
            c = c + 1
        b = b + 1
        c = 1
    a = a + 1
    b = 1
print(a_)
print(b_)
print(c_)
print(a_ * b_ * c_)
# 31875000
