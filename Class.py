import time 
from os import system

def imprimir_pedido():
    itens = []
    i = 0
    with open('pedido.txt' , 'r+') as arq:
        for linha in arq:
            linha = linha.strip(",")
            itens.append(linha.split())       
        
        for iten in itens:
            print("**********************************")
            print('''* {} {}''' .format(itens[i][0]))

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
            time.sleep(1.3)

def escolhas(temH):
    if temH == True:
        eB = input("Deseja escolher adicionar alguma bebida ? (S/N) ") .upper()
        if eB == 'S':
            bebida,valorB,quanB = bebidas()
            time.sleep(0.6)
        else:
            print("Sem bebidas hoje! Anotado.")
            bebida,valorB,quanB = 0,0,0
            time.sleep(0.6)

        eA = input("Deseja escolher adicionar algum acompanhamento ? (S/N) ") .upper()
        if eA == 'S':
            acc,valorA,quanA = acompanhamentos()
            time.sleep(0.6)
        else:
            print("Sem acompanhamentos hoje! Anotado.")
            acc,valorA,quanA = 0,0,0
            time.sleep(0.6)

        eS = input("Deseja escolher adicionar alguma sobremesa ? (S/N) ") .upper()
        if eS == 'S':
            sobrem,valorS,quanS = sobremesas()
            time.sleep(0.6)
        else:
            print("Sem sobremesas hoje! Anotado.")
            sobrem,valorS,quanS = 0,0,0
            time.sleep(0.6)

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

    else:
        eH = input("Deseja escolher adicionar algum hambúrguer ? (S/N) ") .upper()
        if eH == 'S':
            ham = 2
        else:
            #return ham,valorH,quanH,promocao,valorP,quanP,bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb 
            print("")  

def adicionarArquivo(valorT,ham,valorH,quanH,promocao,valorP,quanP,bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb):
    with open('pedido.txt' , 'w+') as arq:
            arq.writelines(f'{valorT}-{ham},{valorH},{quanH}-{promocao},{valorP},{quanP}-{bebida},{valorB},{quanB}-{acc},{valorA},{quanA}-{sobrem},{valorS},{quanS}-{bebidaQuente},{valorBQ},{quanBQ}-{alt}-{obb}\n')
            arq.seek(0)
            print("Pedido feito com sucesso")
            system('cls')
            time.sleep(0.4)
            print("Imprimindo seu pedido .")
            system('cls')
            time.sleep(0.4)
            print("Imprimindo seu pedido ..")
            system('cls')
            time.sleep(0.4)
            print("Imprimindo seu pedido ...")
            time.sleep(1)
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
            ham = 'CalebeBurger'
            valorH = 15.00
            quanH = get_quantidade()
            quanP,promocao,valorP = promocoes()
            temH = True
            bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb = escolhas(temH)
            pedido(ham,valorH,quanH,promocao,valorP,quanP,bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb)
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
            bebida = 'LataRefri'
            valorB = 4.00
            quanB = get_quantidade()
            return bebida, valorB, quanB
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
            acc = 'AneisDecebola'
            valorA = 11.00
            quanA = get_quantidade()
            return acc, valorA, quanA
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
    print("* 4 - Chocolate       | R$ 2,00  *")
    print("* 4 - PeitinDeGato    | R$ 7,00  *")
    print("* 0 - Cancelar pedido            *")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            sobrem = 'Sorvete'
            valorS = 3.75
            quanS = get_quantidade()
            return sobrem, valorS, quanS
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
            bebidaQuente = 'Cafe'
            valorBQ = 3.00
            quanBQ = get_quantidade()
            return bebidaQuente, valorBQ, quanBQ
    time.sleep(1)

def tela1():
    system('cls')
    print("**********************************")
    print("* Bem vindo ao Calebe's Burger ! *")
    print("**********************************")
    time.sleep(1)
    produtos()

def promocoes():
    system('cls')
    print("**********************************")
    print("*        Calebe's Burger !       *")
    print("**********************************")
    print("*           Promoções            *")
    print("**********************************")
    print("""* 1 - Batata M + Refri Lata    | Por + R$ 8,00  *
* 2 - Batata G + Refri 1 Litro | Por + R$ 14,00 *
* 3 - Kit Fome (Batata G + Refri 2 Litros +
* Anéis de cebola + 1 Musse)   | Por + R$ 19,50 *
* 4 - Kit Petisco (Anéis de cebola + Camarão    *
* frito + Frango frito + Cerveja + Energético   *
* + Refrigerante 2 Litros)     | Por + R$ 49,00 *
* 5 - BaconBurger              | Por + R$ 10,00 *
* 6 - Nenhuma promoção         | Free           *
* 0 - Cancelar pedido          | De graça :)    *""")
    print("**********************************")
    opcao = get_opcao()
    if opcao != 0:
        if opcao == 1:
            promocao = 'BatataM+RefriLata'
            valorP = 8.00
            quanP = get_quantidade()
            return quanP,promocao, valorP
    else:
        cancelarPedido()

def pedido(ham,valorH,quanH,promocao,valorP,quanP,bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb):
    ham = ham
    valorH = valorH
    quanH = quanH
    promocao = promocao
    valorP = valorP
    quanP = quanP
    bebida = bebida
    valorB = valorB
    quanB = quanB
    acc = acc
    valorA = valorA
    quanA = quanA
    sobrem = sobrem
    valorS = valorS
    quanS = quanS
    bebidaQuente = bebidaQuente
    valorBQ = valorBQ
    quanBQ = quanBQ
    alt = alt
    obb = obb
    valorT = valorH * quanH + valorP * quanP + valorB * quanB + valorA * quanA + valorS * quanS + valorBQ * quanBQ
    
    adicionarArquivo(valorT,ham,valorH,quanH,promocao,valorP,quanP,bebida,valorB,quanB,acc,valorA,quanA,sobrem,valorS,quanS,bebidaQuente,valorBQ,quanBQ,alt,obb)

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
    else:
        cancelarPedido()
        time.sleep(1)
