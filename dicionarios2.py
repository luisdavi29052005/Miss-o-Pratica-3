# dicionarios2.py

# Criação do dicionário
meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

# Atualizando o dicionário
meu_dicionario.update({2: {'nome': 'João', 'idade': 32, 'nacionalidade': 'português'}})
print("Dicionário atualizado:", meu_dicionario)

# Criando uma cópia do dicionário
copia_dicionario = meu_dicionario.copy()
print("Cópia do dicionário:", copia_dicionario)

# Removendo um elemento com pop
meu_dicionario.pop(1)
print("Dicionário após remover o elemento 1:", meu_dicionario)

# Removendo o último elemento com popitem
meu_dicionario.popitem()
print("Dicionário após remover o último elemento:", meu_dicionario)

# Limpando ambos os dicionários
meu_dicionario.clear()
copia_dicionario.clear()
print("Dicionário original após clear:", meu_dicionario)
print("Cópia do dicionário após clear:", copia_dicionario)

# Criando um novo dicionário com fromKeys
novo_dicionario = dict.fromkeys(['chave1', 'chave2'], 'valor')
print("Novo dicionário:", novo_dicionario)

# Imprimindo itens, chaves e valores
print("Items do novo dicionário:", novo_dicionario.items())
print("Chaves do novo dicionário:", novo_dicionario.keys())
print("Valores do novo dicionário:", novo_dicionario.values())
