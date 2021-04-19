# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# cria loop "infinito";
while True:
  	# armazena o valor do raio digitado na variável;
    radius = float(input('Digite o raio do círculo: '))
    # declara a variável "pi";
    pi = 3.14
    # salva o cálculo solicitado na variável "area";
    area = pi * (radius ** 2)
    # imprime a área do círculo;
    print(f'A área do círculo é {area:.2f}m².')
    # dá a opção do usuário prosseguir ou não;
    option = str(input('Deseja continuar? {S/N] ')).upper()
    # imprime linha "------"
    print('-' * 30)
    # condicional para prosseguir ou não;
    if option not in 'S':
      	# se for não for "S", o programa encerra;
        break
# imprime mensagem final.
print('Muito obrigado e até a próxima!!')