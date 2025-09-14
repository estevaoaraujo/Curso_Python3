"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

ligado = True


while ligado:
    lista =[100]
    print('-----SyStem Compre------')
    print('----------Menu--------')
    print("---- 1 - Inserir compras----")
    print("---- 2 - apagar compras-----")
    print("---- 3 - listar compras-----")
    print("---- 4 - sair---------------")

    play = int(input(f'Escolha: '))

    if play == 1:
        compras = input("1 : ")
        lista.append(compras)
        print(lista)

    