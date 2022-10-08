'''
3°) Crie um algoritmo que irá calcular a nota com 2 fluxos.
No primeiro se for escolhio o tipo aritimético, o algoritmo será responsável por soma as notas e dividir pela quantidade.
Caso seja escolhido o ponderado, você deverá alocar os pesos e fazer uma formula para o cálculo baseado nos pesos escolhios.
'''

notas = (8.7,3.5,9.0,10,6.6,7.2,2.3,0)
pesos = (3,1,2,1,4,5,2,3)
qt = 0
soma = 0
peso = 0

metodo = input('ponderada ou aritmética?\n').lower().replace('é','e')

if metodo == 'aritmetica':
    for i in notas:
        qt += 1
        soma += i
    print(f'a média é: {soma/qt:.2f}')
elif metodo == 'ponderada':
    for i in range(1,len(notas)):
        peso = pesos[i]
        qt += peso
        soma += (peso*notas[i])
    print(f'a média é: {soma/qt:.2f}')
