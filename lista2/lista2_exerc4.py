inputzin = int(input("digita algo ai manzinho: "))

if(inputzin % 2 == 0 and inputzin > 0):
    print("omg ele é par, e positivo")
elif(inputzin % 2 != 0 and inputzin > 0):
    print("omg ele é impar, e positivo")
elif(inputzin % 2 == 0 and inputzin < 0):
    print("omg ele é par, e negativo")
elif(inputzin % 2 != 0 and inputzin < 0):
    print("omg ele é impar, e negativo")
    