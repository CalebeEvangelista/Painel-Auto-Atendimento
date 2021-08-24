itens = []
itens2 = []
i = 0
j = 0

with open('pedido.txt' , 'r+') as arq:
    for linha in arq:
        linha = linha.strip()
        itens.append(linha.split('-'))
        print(itens)   

    for item in itens[0]:
        item = item.strip()
        itens2.append(item.split(','))
        i = i + 1
        j = j + 1
    print(itens2)

    for item in itens2:
        i = 1
        valor = float(itens2[i][i])
        quantidade = float(itens2[i][i+1])
        soma = valor * quantidade
        print(soma)