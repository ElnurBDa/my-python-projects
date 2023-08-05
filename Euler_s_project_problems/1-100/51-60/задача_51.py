def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x']
numbers = []
for d1 in digits:
    for d2 in digits:
        for d3 in digits:
            for d4 in digits:
                for d5 in digits:
                    for d6 in digits:
                        numbers.append(d1 + d2 + d3 + d4 + d5 + d6)
mumbers = numbers[1::]
numbers = []
for number in mumbers:
    whatisit = True
    while whatisit:
        if number[0] == '0':
            number = number[1::]
        else:
            whatisit = False
    if number.count('x') > 0 and number[-1] not in ['2', '4', '6', '8', '0']:
        numbers.append(number)

print(len(numbers), " numbers")

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
record = [0, 0]
ooo = []
for number in numbers:
    count = 0
    for digit in digits:
        a = number.replace('x', digit)
        if is_prime(int(a)) and a[0] != '0':
            count += 1
    if count >= record[1]:
        record = [number, count]
        ooo.append(record)
print(record)
print(ooo)
# ['x2x3x3', 8]
