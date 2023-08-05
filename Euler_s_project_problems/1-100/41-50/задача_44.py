limit = 5000
limit_ = 10000
pentagonal_nums = []
for x in range(1, int(limit_)):
    pentagonal_nums.append(x * (3 * x - 1) / 2)


def p(n):
    return n * (3 * n - 1) / 2


for a in range(1000, limit):
    for b in range(2000, limit):
        if abs(p(a) - p(b)) in pentagonal_nums and p(a) + p(b) in pentagonal_nums:
            print(a, p(a), b, p(b))


#a, p(a), b, p(b)
#1020 1560090.0 2167 7042750.0