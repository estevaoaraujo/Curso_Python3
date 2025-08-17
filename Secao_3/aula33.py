"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_int = input("Digite número: ")

numero_int = int(numero_int)

if numero_int % 2 == 0:
    print(f" Voce digitou {numero_int} e par")
else:
    print(f"Voce digitou {numero_int} e impar")    