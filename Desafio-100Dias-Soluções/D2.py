print("Seja bem vindo(a) à Calculadora de Troco")
conta = int(input(f'Por favor, informe o valor total da conta: R$ '))
gorjeta = int(input(f'Por favor, informe quanto de gorjeta gostaria de deixar (5, 10, 12, 15): '))
pessoas = int(input(f'Por favor, informe quantas pessoas dividirão a conta: '))
gorjeta_real = ((gorjeta / 100) + 1)
valor = ((conta * gorjeta_real) / pessoas)
print('O valor que cada pessoa deverá pagar é de: R$ {}'.format(valor))
