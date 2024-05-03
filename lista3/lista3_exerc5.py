coisa = range(233,456)
count = 233

for i in coisa:
    while count <= 456:
        if count >= 300 and count <= 400:
            count = count + 3
            print(count)
        else:
            count = count + 5
            print(count)