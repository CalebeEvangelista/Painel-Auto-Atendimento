import time 
from os import system

def limparArquivo():
    with open("pedido.txt","w+") as arq:
        arq.writelines('')

def imprimir_pedido():
    system('cls')
    print("Pedido feito com sucesso")
    time.sleep(1)
    system('cls')
    print("Imprimindo seu pedido .")
    time.sleep(1)
    system('cls')
    print("Imprimindo seu pedido ..")
    time.sleep(1)
    system('cls')
    print("Imprimindo seu pedido ...")
    time.sleep(1)

    itens = []
    itens2 = []
    h = 1
    i = 0
    j = 2
    total = 0

    with open('pedido.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip()
            itens.append(linha.split('-')) 

        for item in itens[0]:
            item = item.strip()
            itens2.append(item.split(','))

        try:
            system('cls')
            print("**********************************")
            print("*        Calebe's Burger !       *")
            print("**********************************")
            print("*         Cupom fiscal!          *")
            print("**********************************")
            for item in itens2:
                if itens2[i][h] and itens2[i][j] == '0':
                    del(itens2[i])
                    i -= 1
                elif itens2[i][h] and itens2[i][j] != '0':
                    valor = float(itens2[i][h])
                    quantidade = float(itens2[i][j])
                    soma = valor * quantidade
                    mostrar = int(quantidade)
                    print('''* {}x {} - Total de R$ {}''' .format(mostrar, itens2[i][0], soma))
                    print('**********************************')
                    time.sleep(0.5)
                    total += soma
                i += 1

        finally:
            print("* O valor total do pedido é R${} *" .format(total))
            print('**********************************')
            opcao = input("Digite qualquer tecla para finalizar seu pagamento!")
            system('cls')
            print("Pagamento realizado com sucesso!")
            time.sleep(1)
            return

def get_opcao():
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            return opcao
        except:
            print("Por favor digite um numero valido!")

def get_quantidade():
    while True:
        try:
            quantidade = float(input("Insira a quantidade:"))
            return quantidade
        except:
            print("Por favor insira uma quantidade valida!")
            time.sleep(1)

def escolhas(temH,temB,temA,temS,temBQ):
    if temH == False:
        eH = input("Deseja escolher adicionar algum hambúrguer ? (S/N) ") .upper()
        if eH == 'S':
            print('')
    elif temB == False:
        eB = input("Deseja escolher adicionar alguma bebida ? (S/N) ") .upper()
        if eB == 'S':
            bebida,valorB,quanB = bebidas()
            time.sleep(0.6)
        else:
            print("Sem bebidas hoje! Anotado.")
            bebida,valorB,quanB = 0,0,0
            time.sleep(0.6)
    elif temA == False:
        eA = input("Deseja escolher adicionar algum acompanhamento ? (S/N) ") .upper()
        if eA == 'S':
            acc,valorA,quanA = acompanhamentos()
            time.sleep(0.6)
        else:
            print("Sem acompanhamentos hoje! Anotado.")
            acc,valorA,quanA = 0,0,0
            time.sleep(0.6)
    elif temS == False:
        eS = input("Deseja escolher adicionar alguma sobremesa ? (S/N) ") .upper()
        if eS == 'S':
            sobrem,valorS,quanS = sobremesas()
            time.sleep(0.6)
        else:
            print("Sem sobremesas hoje! Anotado.")
            sobrem,valorS,quanS = 0,0,0
            time.sleep(0.6)
    elif temBQ == False:
        eBQ = input("Deseja escolher adicionar alguma bebida quente ? (S/N) ") .upper()
        if eBQ == 'S':
            bebidaQuente,valorBQ,quanBQ = bebidasQuentes()
            time.sleep(0.6)
        else:
            print("Sem bebidas quentes hoje! Anotado.")
            bebidaQuente,valorBQ,quanBQ = 0,0,0
            time.sleep(0.6)

        #eAlt = input("Deseja escolher adicionar algum acompanhamento ? (S/N) ") .upper()
        #if eAlt == 'S':
        alt = 'Nao'

        #eObs = input("Deseja escolher adicionar algum acompanhamento ? (S/N) ") .upper()
        #if eObs == 'S':
        obb = 'Nao'

    return bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb 

def adicionarArquivo(nome,valor,quant):
    with open('pedido.txt' , 'a+') as arq:
            arq.writelines(f'{nome},{valor},{quant}-')
            arq.seek(0)
            escolha = input("Deseja adicionar mais produtos ao seu pedido ? (S/N) ") .upper()
            if escolha == 'S':
                tela1()
            else:
                imprimir_pedido()

def hamburger():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*          Hambúrgueres          *")
    print("**********************************")
    print("* 1 - Calebe Burger   | R$ 15,00 *")
    print("* 2 - X-Tudo          | R$ 9,00  *")
    print("* 3 - X-Frango        | R$ 7,00  *")
    print("* 4 - Ricardão        | R$ 4,00  *")
    print("* 5 - BaconBurger     | R$ 10,00 *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'CalebeBurger'
            valor = 15.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'X-Tudo'
            valor = 9.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'X-Frango'
            valor = 7.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 4:
            nome = 'Ricardão'
            valor = 4.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 5:
            nome = 'BaconBurger'
            valor = 10.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    else:
        cancelarPedido()
    time.sleep(1)

def bebidas():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*            Bebidas             *")
    print("**********************************")
    print("* 1 - Lata de Refri   | R$ 4,00  *")
    print("* 2 - Refri 1 litro   | R$ 6,00  *")
    print("* 3 - Refri 2 litros  | R$ 8,00  *")
    print("* 4 - Cerveja         | R$ 7,00  *")
    print("* 5 - Energético      | R$ 10,00 *")
    print("* 6 - Agua            | R$ 1,00  *")
    print("* 7 - Jarra de suco   | R$ 6,00  *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'LataRefri'
            valor = 4.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'Refri1Litro'
            valor = 6.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'Refri2Litros'
            valor = 8.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 4:
            nome = 'Cerveja'
            valor = 7.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 5:
            nome = 'Energético'
            valor = 10.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 6:
            nome = 'Agua'
            valor = 1.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 7:
            nome = 'JarraDeSuco'
            valor = 6.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    else:
        cancelarPedido()
    time.sleep(1)
    
def acompanhamentos():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*         Acompanhamentos        *")
    print("**********************************")
    print("* 1 - Anéis de cebola | R$ 11,00 *")
    print("* 2 - Camarão frito   | R$ 19,90 *")
    print("* 3 - Batata Frita P  | R$ 2,50  *")
    print("* 4 - Batata Frita M  | R$ 5,00  *")
    print("* 5 - Batata Frita G  | R$ 10,00 *")
    print("* 6 - Espetinho       | R$ 5,00  *")
    print("* 7 - Espetinho carne | R$ 5,00  *")
    print("* 8 - Frango Frito    | R$ 5,00  *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'AnéisDeCebola'
            valor = 11.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'CamarãoFrito'
            valor = 19.90
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'BatataFritaP'
            valor = 2.50
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 4:
            nome = 'BatataFritaM'
            valor = 5.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 5:
            nome = 'BatataFritaG'
            valor = 10.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 6:
            nome = 'Espetinho'
            valor = 5.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 7:
            nome = 'Espetinho carne'
            valor = 5.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 8:
            nome = 'Frango Frito'
            valor = 5.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    else:
        cancelarPedido()
    time.sleep(1)

def sobremesas():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*           Sobremesas           *")
    print("**********************************")
    print("* 1 - Sorvete         | R$ 3,75  *")
    print("* 2 - Pudim           | R$ 2,00  *")
    print("* 3 - Musse           | R$ 2,50  *")
    print("* 4 - Goiabada        | R$ 3,00  *")
    print("* 5 - DinDin Gourmet  | R$ 5,00  *")
    print("* 6 - Chocolate       | R$ 2,00  *")
    print("* 7 - Peitin De Gato  | R$ 7,00  *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'Sorvete'
            valor = 3.75
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'Pudim'
            valor = 2.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'Musse'
            valor = 2.50
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 4:
            nome = 'Goiabada'
            valor = 3.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 5:
            nome = 'DinDin Gourmet'
            valor = 5.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 6:
            nome = 'Chocolate'
            valor = 2.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 7:
            nome = 'PeitinDeGato'
            valor = 7.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    else:
        cancelarPedido()
    time.sleep(1)

def bebidasQuentes():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*        Bebidas quentes         *")
    print("**********************************")
    print("* 1 - Café            | R$ 3,00  *")
    print("* 2 - Chá             | R$ 4,00  *")
    print("* 3 - Coca de ontem   | R$ 1,00  *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'Café'
            valor = 3.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'Chá'
            valor = 4.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'CocaDeOntem'
            valor = 1.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    time.sleep(1)

def promocoes():
    system('cls')
    print("*************************************************")
    print("*                 Calebe's Burger !             *")
    print("*************************************************")
    print("*                    Promoções                  *")
    print("*************************************************")
    print("""* 1 - Batata M + Refri Lata    | Por + R$ 8,00  *
* 2 - Batata G + Refri 1 Litro | Por + R$ 14,00 *
* 3 - Kit Fome (Batata G + Refri 2 Litros +
* Anéis de cebola + 1 Musse)   | Por + R$ 19,50 *
* 4 - Kit Petisco (Anéis de cebola + Camarão    *
* frito + Frango frito + Cerveja + Energético   *
* + Refrigerante 2 Litros)     | Por + R$ 49,00 *
* 0 - Cancelar pedido          | De graça :)    *""")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            nome = 'BatataM+RefriLata'
            valor = 8.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 2:
            nome = 'BatataG+Refri1Litro'
            valor = 14.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 3:
            nome = 'KitFome'
            valor = 19.50
            quant = get_quantidade()
            pedido(nome,valor,quant)
        if opcao == 4:
            nome = 'Kit Petisco'
            valor = 49.00
            quant = get_quantidade()
            pedido(nome,valor,quant)
    else:
        cancelarPedido()

def pedido(nome,valor,quant):
    nome = nome
    valor = valor
    quant = quant
    adicionarArquivo(nome,valor,quant)

def cancelarPedido():
    print("Pedido Cancelado!")

def produtos():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*      Escolha uma categoria:    *")
    print("**********************************")
    print("* 1 - Hambúrguer                 *")
    print("* 2 - Bebidas                    *")
    print("* 3 - Acompanhamentos            *")
    print("* 4 - Sobremesas                 *")
    print("* 5 - Bebidas quentes            *")
    print("* 6 - Promoções                  *")
    print("* 9 - Finalizar pedido           *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()

    if opcao != 0:
        if opcao == 1:
            hamburger()
            time.sleep(1)

        if opcao == 2:
            bebidas()
            time.sleep(1)

        if opcao == 3:
            acompanhamentos()
            time.sleep(1)
            
        if opcao == 4:
            sobremesas()
            time.sleep(1)

        if opcao == 5:
            bebidasQuentes()
            time.sleep(1)
        
        if opcao == 6:
            promocoes()
            time.sleep(1)

        if opcao == 9:
            imprimir_pedido()
            time.sleep(1)
    
    else:
        cancelarPedido()
        time.sleep(1)

def tela1():
    system('cls')
    print("**********************************")
    print("* Bem vindo ao Calebe's Burger ! *")
    print("**********************************")
    time.sleep(1)
    produtos()