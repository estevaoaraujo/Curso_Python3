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

