def crypter(data, key):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    new_data = ''
    if key>len(SYMBOLS):
        return 'key is big\nchange it to smaller one!'
    for x in range(len(data)):
        if key+SYMBOLS.index(data[x])>=len(SYMBOLS):
            new_data += SYMBOLS[key + SYMBOLS.index(data[x])-len(SYMBOLS)]
        else:
            new_data+=SYMBOLS[key+SYMBOLS.index(data[x])]
    return new_data

for x in range(66):
    print(encrypter('Elnur is great!',key=x))

