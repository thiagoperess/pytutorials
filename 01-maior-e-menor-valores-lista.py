# MAIOR E MENOR VALORES DA LISTA:

# criando uma lista para armazenar os valores;
lista = []
# criando um loop para coleta dos valores;
for p in range(1, 6):
    # entrada para armazenamento dos valores;
    values = float(input(f'Peso da {p}ª pessoa: '))
    # adiciona os valores à lista a cada 'volta' do loop;
    lista += [values]
# printa o maior valor da lista com a função built-in 'max';
print(f'O maior peso lido foi {max(lista):.2f} Kg.')
# printa o menor valor da lista com a função built-in 'min';
print(f'O menor peso lido foi {min(lista):.2f} Kg.')