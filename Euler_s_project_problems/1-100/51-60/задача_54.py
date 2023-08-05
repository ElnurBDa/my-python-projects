

dictionary = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, }


def card_value(a):
    global dictionary
    b = []
    for x in a:
        b.append(dictionary[x[0]])
    return b


def value_repeat_count(a):
    b = card_value(a)
    c = []
    for x in range(2, 15):
        c.append(b.count(x))
    return c


def high_card(a):
    b = card_value(a)
    return max(b)


def one_pair(a):
    if value_repeat_count(a).count(2) == 1:
        return value_repeat_count(a).index(2) + 2
    return 0


def two_pairs(a):
    if value_repeat_count(a).count(2) == 2:
        return value_repeat_count(a).index(2) + 2, value_repeat_count(a).index(2, 2) + 2
    return 0,0


def three_of_a_Kind(a):
    if value_repeat_count(a).count(2) == 1 and value_repeat_count(a).count(3) == 1:
        return 0
    elif value_repeat_count(a).count(3) == 1:
        return value_repeat_count(a).index(3) + 2
    return 0


def straight(a):
    b = card_value(a)
    for x in b:
        if x - 1 in b and x - 2 in b and x - 3 in b and x - 4 in b:
            return max(b)
    return 0


def flush(a):
    if a[0][1] == a[1][1] == a[2][1] == a[3][1] == a[4][1]:
        return True
    return 0


def full_house(a):
    if value_repeat_count(a).count(2) == 1 and value_repeat_count(a).count(3) == 1:
        return value_repeat_count(a).index(2) + 2, value_repeat_count(a).index(3) + 2
    return 0,0


def four_of_a_kind(a):
    if value_repeat_count(a).count(4) == 1:
        return value_repeat_count(a).index(4) + 2
    return 0


def straight_flush(a):
    if flush(a) and straight(a):
        return straight(a)
    return 0


def royal_flush(a):
    b = card_value(a)
    b.sort()
    if b == [10, 11, 12, 13, 14] and a[0][1] == a[1][1] == a[2][1] == a[3][1] == a[4][1]:
        return True
    return 0


def poker(r, q):
    if royal_flush(r):
        return 'r'
    elif royal_flush(q):
        return 'q'
    else:
        if straight_flush(r) > straight_flush(q):
            return 'r'
        elif straight_flush(q) > straight_flush(r):
            return 'q'
        else:
            if four_of_a_kind(r) > four_of_a_kind(q):
                return 'r'
            elif four_of_a_kind(q) > four_of_a_kind(r):
                return 'q'
            else:
                if full_house(r)[1] > full_house(q)[1]:
                    return 'r'
                elif full_house(q)[1] > full_house(r)[1]:
                    return 'q'
                else:
                    if full_house(q)[0] > full_house(r)[0]:
                        return 'q'
                    else:
                        if flush(r):
                            return 'r'
                        elif flush(q):
                            return 'q'
                        else:
                            if straight(r) > straight(q):
                                return 'r'
                            elif straight(q) > straight(r):
                                return 'q'
                            else:
                                if three_of_a_Kind(r) > three_of_a_Kind(q):
                                    return 'r'
                                elif three_of_a_Kind(q) > three_of_a_Kind(r):
                                    return 'q'
                                else:
                                    if two_pairs(r)[0] > two_pairs(q)[0]:
                                        return 'r'
                                    elif two_pairs(q)[0] > two_pairs(r)[0]:
                                        return 'q'
                                    else:
                                        if two_pairs(r)[1] > two_pairs(q)[1]:
                                            return 'r'
                                        elif two_pairs(q)[1] > two_pairs(r)[1]:
                                            return 'q'
                                        else:
                                            if one_pair(r) > one_pair(q):
                                                return 'r'
                                            elif one_pair(q) > one_pair(r):
                                                return 'q'
                                            else:
                                                if high_card(r) > high_card(q):
                                                    return 'r'
                                                elif high_card(q) > high_card(r):
                                                    return 'q'
                                                else:
                                                    return 'WTF!'




b = []
file = open('hands.txt', 'r')
data = file.read()
count = 0
st = ''
for x in data:
    st += x
    count += 1
    if count == 30:
        count = 0
        b.append(st[:-1])
        st = ''
b.append(st)
file.close()

count_1 = 0
count_2 = 0

for x in b:
    r = [x[0:2], x[3:5], x[6:8], x[9:11], x[12:14]]
    q = [x[15:17], x[18:20], x[21:23], x[24:26], x[27:29]]
    if poker(r,q)=='r':
        count_1+=1
    elif poker(r,q)=='q':
        count_2+=1
    else:
        print(r,q,poker(r,q))
print(count_1)
print(count_2)
print()


