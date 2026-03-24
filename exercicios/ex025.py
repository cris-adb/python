# Tabela Hash simplificada.
# Para isso, não usaremos o dicionário pronto. Vamos usar uma Lista (Array) de tamanho fixo e uma função matemática para decidir onde cada item entra.
# A Estrutura Básica
# Nossa tabela terá:

# Um tamanho fixo (ex: 10 posições).

# Uma função hash simples (usaremos o operador % de resto de divisão).

# Tratamento de colisão usando Encadeamento (cada posição da lista será uma sub-lista).

class MinhaTabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        # Criamos uma lista de listas (baldes) para lidar com colisões
        self.tabela = [[] for _ in range(self.tamanho)]

    def _funcao_hash(self, chave):
        # Transforma a chave em um índice dentro do intervalo [0, tamanho-1]
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        
        # Se a chave já existe, atualizamos o valor
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        
        # Se for nova, adicionamos o par [chave, valor] na lista
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return "Não encontrado"

# --- Testando nossa criação ---
meu_dict = MinhaTabelaHash(tamanho=2)

meu_dict.inserir("Python", 1991)
meu_dict.inserir("Java", 1995)
meu_dict.inserir("JavaScript", 1995)

print(f"Ano do Python: {meu_dict.buscar('Python')}")
print(f"Estado interno da tabela: {meu_dict.tabela}")

# O que aconteceu aqui?
# O Hash: Quando você inseriu "Python", a função hash("Python") % 5 retornou um número (digamos, o índice 3).

# O Armazenamento: O valor 1991 foi guardado na posição 3 da nossa lista principal.

# A Colisão (O pulo do gato): Se hash("Java") % 5 também retornar 3, nossa lista na posição 3 ficará assim: [["Python", 1991], ["Java", 1995]].

# A  Busca: Para achar o "Java", o Python vai direto no índice 3 e percorre apenas aquela pequena sub-lista interna, em vez de olhar a tabela inteira.

# Por que o dict real é melhor?
# O dicionário padrão do Python é extremamente otimizado em C. Ele usa uma técnica chamada Open Addressing (Endereçamento Aberto), que evita criar sub-listas e mantém os dados em um array contíguo na memória, o que é muito mais rápido para o processador ler.
