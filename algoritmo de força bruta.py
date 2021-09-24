
from itertools import permutations
from timeit import default_timer as timer


def forcaBruta(matrix):
    nodos, listaArvore = gerarCaminhos(matrix)

    lista_custo = []
    for ciclo in listaArvore:
        custoCiclo = 0
        for index in range(0, (len(nodos) - 1)):
            custoCiclo = custoCiclo + matrix[ciclo[index]][ciclo[index+1]]
        lista_custo.append(custoCiclo)
    menorCusto = min(lista_custo)
    indiceMenorCusto = lista_custo.index(menorCusto)
    matrix_saida = ["Força Bruta", menorCusto,
                    listaArvore[indiceMenorCusto]]

    return matrix_saida

def gerarCaminhos(matrix):

    nodos = [node for node in range(len(matrix))]
    ultimo_nodo = nodos.pop()
    listaPermutacoes = list(permutations(nodos))
    listaArvore = list(map(list, listaPermutacoes))
    for caminho in listaArvore:
        caminho.append(ultimo_nodo)
        caminho.append(caminho[0])

    return nodos, lista_arvore



matrix = [] 


start = timer()
resultado = forcaBruta(matrix)
end = timer()
print(resultado)
print(f'{end - start}s')
