# Diferente do Encadeamento (onde cada posição tem uma "lista de espera"), no Endereçamento Aberto (Open Addressing), todos os itens são guardados diretamente no array principal.

# Se a "gaveta" (índice) calculada pela função hash já estiver ocupada, o algoritmo não cria uma lista ali; em vez disso, ele procura a próxima gaveta vazia seguindo uma regra específica.

# Como funciona (A lógica do Estacionamento) 
# Pense no endereçamento aberto como um estacionamento: você tem uma vaga reservada pelo seu número de hash. Se alguém parou nela, você não "estaciona em cima"; você segue para a próxima vaga livre seguindo uma estratégia.

# Linear Probing (Sondagem Linear) É a técnica mais simples. Se o índice $h$ está ocupado, tentamos $h+1$, depois $h+2$, $h+3$, e assim por diante (fazendo a volta no final do array se necessário). 

# Vantagem: Muito rápido para o processador ler (aproveita o cache da CPU). 
# Problema (Clustering): Cria "blocos" de dados ocupados. Se muitas chaves caem perto umas das outras, a busca vira uma caminhada lenta por um corredor lotado.

# Quadratic Probing (Sondagem Quadrática) 
# Para evitar os blocos do método linear, a distância do salto aumenta ao quadrado: $h+1^2, h+2^2, h+3^2...$

# Vantagem: Espalha melhor os dados que a linear.Problema: Ainda pode criar um padrão de preenchimento chamado "agrupamento secundário".

# Double Hashing (Hash Duplo)É a técnica mais robusta. Se houver colisão, usamos uma segunda função hash para calcular o tamanho do "salto".
# Exemplo: "Se a vaga 5 está ocupada, pule de 3 em 3 vagas até achar uma livre". O "3" é gerado por uma segunda conta.Vantagem: Quase elimina o agrupamento (clustering). É o que chega mais perto de uma distribuição aleatória ideal.

# O Problema da Remoção: O "Lápide" (Tombstone)Aqui mora um perigo: se você remove um item da posição 5, e o item que você procura no futuro "pulou" pela posição 5 para chegar na 6, a busca pode achar que o item não existe porque encontrou um buraco vazio.Solução: Quando deletamos algo no endereçamento aberto, colocamos um marcador especial (chamado Dummy ou Tombstone). Ele diz: "Aqui está vazio agora, mas continue procurando porque pode ter algo depois de mim".

# Resizing (Redimensionamento)Tabelas de endereçamento aberto sofrem muito quando ficam cheias. Existe um conceito chamado Fator de Carga ($\alpha$):$$\alpha = \frac{\text{número de itens}}{\text{tamanho da tabela}}$$No Python, quando o dicionário atinge um fator de carga de aproximadamente 2/3 (66%), ele automaticamente cria uma tabela nova, geralmente com o dobro do tamanho, e remapeia (re-hash) todos os itens existentes. Isso garante que a busca continue sendo $O(1)$.Qual o Python usa?O dicionário do Python usa uma variante muito inteligente de Sondagem Combinada. Ele não usa apenas linear ou quadrática simples; ele usa uma fórmula que envolve bits da chave original para garantir que o "salto" seja caótico o suficiente para evitar agrupamentos, mas mantendo a velocidade de acesso à memória.

class TabelaHashAberta:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        # Iniciamos com None (vazio)
        self.chaves = [None] * self.tamanho
        self.valores = [None] * self.tamanho
        self.MARCADOR_DELETADO = object() # Marcador único para itens removidos

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        indice_original = indice

        while self.chaves[indice] is not None and self.chaves[indice] is not self.MARCADOR_DELETADO:
            # Se a chave já existe, atualiza o valor
            if self.chaves[indice] == chave:
                self.valores[indice] = valor
                return
            
            # Colisão! Vai para o próximo (Linear Probing)
            indice = (indice + 1) % self.tamanho
            
            # Se der a volta completa, a tabela está cheia
            if indice == indice_original:
                raise Exception("Tabela Hash cheia!")

        # Encontrou um lugar (None ou DELETADO)
        self.chaves[indice] = chave
        self.valores[indice] = valor

    def buscar(self, chave):
        indice = self._hash(chave)
        indice_original = indice

        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave:
                return self.valores[indice]
            
            indice = (indice + 1) % self.tamanho
            if indice == indice_original:
                break
        
        return "Não encontrado"

    def remover(self, chave):
        indice = self._hash(chave)
        indice_original = indice

        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave:
                # Marcamos como deletado em vez de None
                self.chaves[indice] = self.MARCADOR_DELETADO
                self.valores[indice] = None
                return True
            
            indice = (indice + 1) % self.tamanho
            if indice == indice_original:
                break
        return False

# --- Teste Prático ---
tabela = TabelaHashAberta(tamanho=5)

tabela.inserir("Alice", "123-456")
tabela.inserir("Bob", "999-000") # Digamos que Bob colida com Alice
tabela.remover("Alice")

# Se não tivéssemos o marcador "DELETADO", a busca pelo Bob pararia no buraco da Alice!
print(f"Buscando Bob após deletar Alice: {tabela.buscar('Bob')}")

# Por que usar o object() como marcador?
# No código acima, usamos self.MARCADOR_DELETADO = object().

# Se usássemos apenas None ao remover, o método buscar acharia que a "cadeia" de elementos acabou ali e retornaria "Não encontrado" para itens que foram empurrados para frente na colisão.

# O marcador diz à busca: "Pode continuar procurando, havia algo aqui antes!".