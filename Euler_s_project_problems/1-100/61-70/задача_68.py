digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0

from itertools import permutations

c = 0
for x in permutations(digits):
    s1 = x[0]
    s2 = x[1]
    s3 = x[2]
    s4 = x[3]
    s5 = x[4]
    s6 = x[5]
    s7 = x[6]
    s8 = x[7]
    s9 = x[8]
    s10 = x[9]
    sum1 = s1 + s2 + s5
    sum2 = s2 + s4 + s6
    sum3 = s3 + s5 + s8
    sum4 = s7 + s8 + s9
    sum5 = s4 + s7 + s10
    total_set = []
    d = ''
    if sum1 == sum2 == sum3 == sum4 == sum5:
        set1 = [s1, s2, s5]
        set2 = [s3, s5, s8]
        set3 = [s9, s8, s7]
        set4 = [s10, s7, s4]
        set5 = [s6, s4, s2]
        mn = min(set1[0], set2[0], set5[0], set4[0], set3[0])
        if mn in set1:
            total_set = set1 + set2 + set3 + set4 + set5
        if mn in set2:
            total_set = set2 + set3 + set4 + set5 + set1
        if mn in set3:
            total_set = set3 + set4 + set5 + set1 + set2
        if mn in set4:
            total_set = set4 + set5 + set1 + set2 + set3
        if mn in set5:
            total_set = set5 + set1 + set2 + set3 + set4
        print(total_set)
        for x in total_set:
            d += str(x)
        print(d)
        if int(d) > c and len(d)==16:
            c = int(d)

print(c)
