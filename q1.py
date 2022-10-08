'''
1°) Faça um algoritmo que contenha 3 vetores, o primeiro deve ser um vetor com 30 posições, onde irá conter números inteiros aleatórios. 
Após isso, separe esse vector em mais dois novos vetores onde no primeiro vector deve conter apenas os números pares e outro para números ímpares.
Lembrando, você não deve alocar os valores manualmente, utilize um laço for ou while.
'''

from random import randint
vetor1 = []
listapares = []
listaimpares = []

for i in range(30):
    vetor1.append(randint(-1000,1000))
    
for i in vetor1:
    if i % 2 == 0:
        listapares.append(i)
    else:
        listaimpares.append(i)

print('todos os valores:\n',vetor1)
print('\nvalores pares:\n', listapares)
print('\nvalores impares:\n', listaimpares)
