# Implementação do algoritmo de força bruta
from itertools import permutations
from timeit import default_timer as timer


def gerar_caminhos(matrix):
    # Extrai os nodos da matrix
    nodos = [node for node in range(len(matrix))]
    # Remove a última cidade para gerar permutações não cíclicos
    ultimo_nodo = nodos.pop()
    # Enumera todos os caminhos partindo dos nodos
    lista_permutacoes = list(permutations(nodos))
    # Controi uma árvore
    lista_arvore = list(map(list, lista_permutacoes))

    # Fechando os caminhos / Construindo os ciclos completos
    for caminho in lista_arvore:
        caminho.append(ultimo_nodo)
        caminho.append(caminho[0])

    return nodos, lista_arvore


def forca_bruta(matrix):
    # Gera todos os caminhos possiveis
    nodos, lista_arvore = gerar_caminhos(matrix)

    # Calcula o custo de cada ciclo
    lista_custo = []
    for ciclo in lista_arvore:
        # Inicializa o custo para cada ciclo
        custo_ciclo = 0
        # Converte dois nodos em um ciclo para um índice no array de entrada
        for index in range(0, (len(nodos) - 1)):
            # custo_ciclo é calculado a partir da matriz de entrada e entre
            # dois nodos em um ciclo
            custo_ciclo = custo_ciclo + matrix[ciclo[index]][ciclo[index+1]]
        lista_custo.append(custo_ciclo)

    # Calcula o ciclo de menor custo
    menor_custo = min(lista_custo)
    indice_menor_custo = lista_custo.index(menor_custo)
    matrix_saida = ["Força Bruta", menor_custo,
                    lista_arvore[indice_menor_custo]]

    return matrix_saida


matrix = [] #digite a matriz aqui exemplo: [10,15,16]


start = timer()
resultado = forca_bruta(matrix)
end = timer()
print(resultado)
print(f'{end - start}s')