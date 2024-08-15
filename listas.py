# listas.py

# Criação da lista
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Imprimindo o conteúdo da lista
print("Conteúdo inicial da lista:", lista_mesclada)

# Adicionando um elemento com o método append
lista_mesclada.append(["Lista aninhada"])
print("Conteúdo da lista após o append:", lista_mesclada)

# Inserindo um elemento na posição 4 com o método insert
lista_mesclada.insert(4, 5)
print("Conteúdo da lista após o insert:", lista_mesclada)

# Imprimindo o tamanho atual da lista
print("Tamanho atual da lista:", len(lista_mesclada))

# Removendo o item da posição 1
del lista_mesclada[1]
print("Conteúdo da lista após remover o item na posição 1:", lista_mesclada)

# Criando uma nova lista com os primeiros 4 elementos
nova_lista_mesclada = lista_mesclada[:4]
print("Conteúdo da nova lista:", nova_lista_mesclada)
