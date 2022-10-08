'''
2°) Crie um algoritmo que será responsável por calcular o índice de gordura corporal. 
Na situação do sexo masculino deverá conter os seguintes fluxos: 
menor do que 11% = Atleta,
entre 11% e 13% = bom,
entre 14% e 20% = normal,
entre 21% a 23% = elevado,
acima de 23% = alto

Na situação do sexo feminino:
menor do que 16%= Atleta,
entre 16% e 19% = bom,
entre 20% e 28% = normal,
entre 29% a 31% = elevado,
acima de 31% = alto
'''

peso = float(input('digite o seu peso (em kg): '))
altu = float(input('digite a sua altura (em m): '))
sexo = input('qual seu sexo? (masculino/feminino)').lower()

imc = peso/(altu**2)
if sexo == 'masculino':
    if imc > 23: print('alto')
    elif imc >=21: print('elevado')
    elif imc >=14: print('normal')
    elif imc >=11: print('bom')
    else: print('atleta')
elif sexo == 'feminino':
    if imc > 31: print('alto')
    elif imc >=29: print('elevado')
    elif imc >=20: print('normal')
    elif imc >=16: print('bom')  
    else: print('atleta')
