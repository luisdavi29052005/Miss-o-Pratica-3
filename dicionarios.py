# dicionarios.py

# Criação do dicionário
meu_dicionario = {
    1: 'Python',
    2: 'Java',
    3: 'PHP'
}

# Imprimindo o conteúdo do dicionário
print("Conteúdo do dicionário:", meu_dicionario)

# Imprimindo o tipo do dicionário
print("Tipo do dicionário:", type(meu_dicionario))

# Imprimindo o valor da chave 'linguagem'
print("Valor da chave 2:", meu_dicionario.get(2))

# Imprimindo o tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))

# Criação de um dicionário aninhado
dicionario_frutas = {
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
}

# Imprimindo valores específicos do dicionário aninhado
print("Nome e tipo da fruta 1:", dicionario_frutas[1]['nome'], "-", dicionario_frutas[1]['tipo'])
print("Nome e tipo da fruta 2:", dicionario_frutas[2]['nome'], "-", dicionario_frutas[2]['tipo'])

# Iterando sobre o dicionário aninhado
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave}: Nome = {valor['nome']}, Tipo = {valor['tipo']}")
