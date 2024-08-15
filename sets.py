# sets.py

# Criação do set
set_inicial = {11, 12, 13, 14}

# Imprimindo o conteúdo do set
print("Conteúdo inicial do set:", set_inicial)

# Adicionando um elemento ao set
set_inicial.add(15)
print("Conteúdo do set após adicionar 15:", set_inicial)

# Atualizando o set com novos elementos
set_inicial.update({1, 2, 3, 4, 5})
print("Conteúdo do set após atualização:", set_inicial)

# Removendo o elemento 13 do set
set_inicial.discard(13)
print("Conteúdo do set após remover 13:", set_inicial)

# Criação de um novo set
novo_set = {20, 21, 23, 1, 2}
print("Conteúdo do novo set:", novo_set)

# União dos dois sets
print("União dos sets:", set_inicial.union(novo_set))

# Interseção dos dois sets
print("Interseção dos sets:", set_inicial.intersection(novo_set))

# Diferença entre os dois sets
print("Diferença dos sets:", set_inicial.difference(novo_set))

# Diferença simétrica entre os dois sets
print("Diferença simétrica dos sets:", set_inicial.symmetric_difference(novo_set))
