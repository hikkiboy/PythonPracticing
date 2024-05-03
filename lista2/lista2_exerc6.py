idade = int(input("idade: "))

if(idade >= 5 and idade <= 7):
    print("grupo criança A")
elif(idade >= 8 and idade <= 11):
    print("grupo criança B")
elif(idade >= 12 and idade <= 13):
    print("grupo jovem A")
elif(idade >= 14 and idade <= 17):
    print("grupo jovem B")
else:
    print("adulto")