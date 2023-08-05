import fractions

fore = [1]
for x in range(1, 50):
    fore.append(2 * x)
    fore.append(1)
    fore.append(1)
print(fore)
for i in range(0, 100):
    s = 0
    for x in fore[0:i][::-1]:
        s = fractions.Fraction(1 / (s + x))
    print( s+2,i+1)
sum=0
for x in "6963524437876961749120273824619538346438023188214475670667":
    sum+=int(x)
print(sum)

