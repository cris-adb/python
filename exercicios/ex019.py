# A Busca Sequencial (também conhecida como busca linear) é o método mais simples e direto de encontrar um elemento em uma estrutura de dados.
# Imagine que você está procurando um livro específico em uma prateleira bagunçada: você olha o primeiro, depois o segundo, depois o terceiro, até encontrar o que deseja ou chegar ao fim da estante. Isso é a busca sequencial.
# Como funciona o algoritmo?
# O funcionamento segue um passo a passo lógico e repetitivo:
# Começa no primeiro elemento (índice 0) da lista.
# Compara o elemento atual com o valor que você está procurando (a "chave").
# Se forem iguais, a busca termina com sucesso e retorna a posição.
# Se forem diferentes, ele passa para o próximo elemento.
# Repete os passos até encontrar o item ou percorrer a lista inteira.

def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  # Retorna o índice onde o item foi encontrado
    return -1  # Retorna -1 se o item não existir na lista

# Exemplo de uso:
minha_lista = [10, 23, 45, 70, 11, 15]
resultado = busca_sequencial(minha_lista, 70)

if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado.")

# Quando usar?
# A busca sequencial é a escolha certa quando:
# A sua lista é pequena.
# A sua lista não está ordenada e você não quer gastar tempo ordenando-a.''
# Você está buscando em uma estrutura que só permite acesso sequencial (como uma Lista Encadeada simples).