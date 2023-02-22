def multiplicar_matrizes(matriz1, matriz2):

    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    linhas_matriz2 = len(matriz2)
    colunas_matriz2 = len(matriz2[0])


    if colunas_matriz1 != linhas_matriz2:
        raise ValueError("Erro!!")


    matriz_resultante = [[0 for _ in range(colunas_matriz2)] for _ in range(linhas_matriz1)]


    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(linhas_matriz2):
                matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultante

matriz1 = [[3, 6], [1, 5], [3, 5]]
matriz2 = [[100, 50, 50], [50, 100, 50]]

matriz_resultante = multiplicar_matrizes(matriz1, matriz2)

print(matriz_resultante)