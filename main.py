# main.py

from operacoes import calcular_media, verificar_reprovacao, imprimir_reprovados

# Estrutura de dados dos alunos
alunos = {
    1: {'nome': 'Ana', 'notas': [7, 5, 6, 8]},
    2: {'nome': 'Carlos', 'notas': [4, 3, 5, 4]},
    3: {'nome': 'Maria', 'notas': [9, 8, 7, 10]},
    4: {'nome': 'João', 'notas': [3, 2, 4, 1]},
}

# Lista para armazenar as matrículas dos alunos reprovados
reprovados = []

# Verificação dos alunos reprovados
for matricula, dados in alunos.items():
    media = calcular_media(dados['notas'])
    if verificar_reprovacao(media):
        reprovados.append(matricula)

# Imprimindo os alunos reprovados
imprimir_reprovados(alunos, reprovados)
