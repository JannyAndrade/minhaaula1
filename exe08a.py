numero = int(input('Digite um número inteiro:'))
numero1 = int(input('Digite um número inteiro:'))
soma = numero + numero1

print(f'A soma de {numero} e {numero1} é igual a {soma}')
if numero > numero1:
    print(f'O número {numero} é maior que {numero1}')
elif numero < numero1:
    print(f'O número {numero} é menor que {numero1}')

resultado = soma % 2
print('A soma dos dois é par !' if resultado == 0 else 'soma dos dois é impar!')

quadrado = (numero**2) - (numero1**3)
print(f'O quadrado do primeiro menos o cubo do segundo será: {quadrado}')

dividido0 = soma / 10
dividido1 = soma / 15
dividido2 = soma / 20
print('A soma dividido por 10, 15 e 20 será {:.1f} ,{:.1f} e {:.1f} respectivamente'.format(dividido0, dividido1, dividido2))

print('FIM!')







