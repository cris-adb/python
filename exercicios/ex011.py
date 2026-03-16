# Se as listas, filas e pilhas são estruturas lineares (como uma linha ou uma sequência), as Árvores (Trees) são estruturas hierárquicas. Imagine o sistema de pastas do seu computador ou um organograma de uma empresa: tudo começa em um ponto e se ramifica.
# Anatomia de uma Árvore
# Para entender uma árvore, precisamos conhecer seus componentes:
# Raiz (Root): O nó no topo da árvore (o "pai" de todos).
# Nó (Node): Cada elemento que contém um dado.
# Filhos (Children): Nós que derivam de um nó superior.
# Folhas (Leaves): Nós que não têm filhos (estão nas pontas).
# Árvore Binária (A mais comum)
# Em Python, uma das formas mais famosas de árvore é a Árvore Binária, onde cada nó pode ter, no máximo, dois filhos (esquerda e direita).
# Diferente das listas, o Python não tem uma "Árvore" nativa pronta para usar como o list ou dict. Nós a construímos usando Classes.

# Árvore Binária de Busca (BST)
# A árvore fica realmente poderosa quando aplicamos uma regra de organização:# 
# Valores menores que o pai vão para a esquerda.
# Valores maiores que o pai vão para a direita.
# Isso torna a busca por dados extremamente rápida (logarítmica), muito mais eficiente do que percorrer uma lista gigante item por item.
# Por que usar árvores?
# Busca Rápida: Encontrar um item em uma árvore equilibrada é muito mais rápido que em uma lista.
# Hierarquia: Perfeito para representar diretórios de arquivos ou menus de navegação.
# IA e Jogos: Árvores de decisão são usadas para fazer o computador "escolher" a melhor jogada.
# Como percorrer uma árvore?
# Como não é uma linha reta, existem formas diferentes de "ler" os dados (Travessia):
# In-order (Em ordem): Esquerda -> Raiz -> Direita (Retorna os valores ordenados).
# Pre-order: Raiz -> Esquerda -> Direita.
# Post-order: Esquerda -> Direita -> Raiz.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Criando a estrutura manualmente
raiz = No("Empresa")
raiz.esquerda = No("Departamento de TI")
raiz.direita = No("Departamento de RH")

# Adicionando sub-níveis
raiz.esquerda.esquerda = No("Desenvolvimento")
raiz.esquerda.direita = No("Suporte")

print(f"Raiz: {raiz.valor}")
print(f"Filho da Esquerda: {raiz.esquerda.valor}")
print(f"Sub-nível de TI: {raiz.esquerda.esquerda.valor}")