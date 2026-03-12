# Uma lista é uma coleção ordenada de elementos mutáveis em Python
# Você pode armazenar diferentes tipos de dados (inteiros, strings, floats, etc)
lista = [1, 2, 3, 4, 5]

# Acessar elementos da lista usando índice (começa em 0)
primeiro_elemento = lista[0]  # Retorna 1

# Adicionar elementos à lista
lista.append(6)  # Adiciona 6 ao final da lista

# Remover elementos da lista
lista.remove(3)  # Remove o primeiro elemento com valor 3

# Iterar sobre a lista
for elemento in lista:
	print(elemento)  # Imprime cada elemento

# Comprimento da lista
tamanho = len(lista)  # Retorna a quantidade de elementos
