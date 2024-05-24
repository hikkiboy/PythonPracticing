through = False
def Menu():
    through = True
    while True:
        print('1 - Comprar Pizza\n2 - Sair')
        try:
            opMenu = int(input('Digite o que você quer: '))
            if opMenu == 1 :
                Lista()
            else:
                print('bye')
                break
        except:
            print('você digitou errado provavelmente')

def Lista():
    while True:
        print('1- Mussarela - 50\n2- Calabresa - 50\n3 - Frango e catups\n4 - Voltar')
        try:
            opPizza = int(input('Escolhe um ai: '))
            if opPizza == 1:
                PizzaCall('Mussarela')
                break
            elif opPizza == 2:
                PizzaCall('Calabresa')
                break
            elif opPizza == 3:
                PizzaCall('Frango e catups')
                break
            elif opPizza == 4:
                print('tbm xau')
                break
            else:
                print('digita dnv ai manzinho')
        except:
            print('nao pode isso')



def PizzaCall(pizza):
            endereco = input('digite seu endereço: ')
            print(f'enviaremos uma pizza de {pizza} para {endereco} e vc vai pagar UM MILHÃO DE DOLARES HAHAHAHAHAHAHA')



if through == False:
    Menu()