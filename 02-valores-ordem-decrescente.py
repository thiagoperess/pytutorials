# Faça um Programa que leia três números e mostre-os em ordem decrescente. 

# cria uma lista;
list1 = list()
# cria um loop para armazenar 3 valores;
for i in range(0, 3):
  	# recebe a entrada de dados;
    num = int(input('Digite um número: '))
    # armazena os números na lista;
    list1.append(num)
# imprime os valores ordenados em ordem decrescente.
print(sorted(list1, reverse=True))