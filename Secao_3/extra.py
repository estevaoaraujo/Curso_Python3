import random

nome = random.randint(0, 1)

if nome == 0:   
    result = "Estevão"

if nome == 1:   
    result = "Daniel"


print(result)



nomes = ['Ana', 'Carlos', 'João', 'Maria', 'Estevão']
nome = random.choice(nomes)

print(nome)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------'''

tamanho =''

tamanho = int(input('Digite quantos valores deseja insrerir: '))

tabela = [] 

while tamanho >0:
    tabela.append(input('Digite um valor: '))
    tamanho -=1

print(tabela)


print(f'Qauantidade de valores na tebela {len(tabela)}')

contagem = tabela.count('2')
print(f"O valor '2' aparece {contagem} vezes na lista.")


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------'''

print('----------Big Bugger----------')
print('----------Cardapio----------')
print('1 Sanduíche O Clássico Preço: R$ 25,00 \n 2 - Sanduíche do Chefe  Preço: R$ 35,50 \n 3 - Sanduíche Vegetariano  Preço: R$ 28,00 \n4 - Sanduíche Defumado  Preço: R$ 42,00 ')

nome = input('Cliente: ')

escolha = int(input(f'{nome} Faça seu pedido pedido: '))

cardapio = ['','Sanduíche O Clássico','Sanduíche do Chefe','Sanduíche Vegetariano','Sanduíche Defumado']


pedido = cardapio[escolha]

print(pedido)