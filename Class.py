import time 
from os import system

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
    opcao = int(input("Escolha seu Hambúrguer pelo número: "))
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
    opcao = int(input("Escolha sua bebida pelo número: "))
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
    opcao = int(input("Escolha seu acompanhamento pelo número: "))
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
    opcao = int(input("Escolha sua sobremesa pelo número: "))
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
    opcao = int(input("Escolha sua bebida pelo número: "))
    time.sleep(1)

def tela1():
    system('cls')
    print("**********************************")
    print("* Bem vindo ao Calebe's Burger ! *")
    print("**********************************")
    time.sleep(1)
    produtos()

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
    opcao = int(input("Digite uma opção: "))

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
        print("Pedido Cancelado!")
        time.sleep(1)
