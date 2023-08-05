from time import sleep
try:
    file_input = input("Enter txt file(Example : File.txt): ")
    file = open(file_input, 'r')
    data1 = []
    for a in file:
        a = a[:-1]
        data1.append(a)
    for a in data1:
        print(a)
    file.close()
    want = input("Enter + if you want to change it : ")
    if want == '+':
        data2 = []
        z = 1
        for x in data1:
            if x != "":
                b = str(z) + ") " + x[0].upper() + x[1:] + " ."
                z += 1
                data2.append(b)
        file = open(file_input, 'w+')
        for a in data2:
            file.write(a + "\n")
        file.close()
except:
    print("Error")
    sleep(2)