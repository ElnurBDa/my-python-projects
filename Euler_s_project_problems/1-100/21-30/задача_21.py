def d(n):
    d = 0
    for x in range(1, n):
        if n % x == 0:
            d += x
    return d


from time import time

start = time()
c = 0
n = 1
till = 10001
a = []
for x in range(n, till):
    for y in range(n, till):
        if d(x) == y and d(y) == x and x != y:
            f = open('progress_для_задачи_21.txt', 'w+')
            c += 1
            print(d(x), d(y))
            print(c)
            timer = time() - start
            a.append(str(c) + ') d(x)= ' + str(y) + '  d(y)= ' + str(x) + '  Time= ' + str(timer))
            for z in a:
                f.write(z + '\n')
            f.close()
    n += 1
    if n == till:
        break
print('____')
print(c)
end = time()
print(end - start)
f = open('total_для_задачи_21.txt', 'w+')
f.write('Total = ' + str(c) + '\n' + 'Total time = ' + str(end - start))
f.close()
'''
1) 284 220
2) 1210 1184

'''
