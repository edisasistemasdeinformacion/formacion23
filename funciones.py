def fibonacci(n):
    fib_array = [0, 1]

    for i in range(2, n):
        fib_array.append(fib_array[-1] + fib_array[-2])

    return fib_array


    def floyd_warshall_jorge(graph):
    """
    Encuentra todos los caminos más cortos entre cada par de nodos en un grafo ponderado.

    :param graph: Una matriz de adyacencia representando el grafo ponderado.
                  graph[i][j] = peso de la arista de i a j, o float('inf') si no hay arista.
    :return: Una matriz de distancias mínimas entre cada par de nodos.
    """
    num_nodos = len(graph)

    # Inicializar la matriz de distancias mínimas
    distancias = [[float('inf') if i != j else 0 for j in range(num_nodos)] for i in range(num_nodos)]

    # Actualizar la matriz de distancias con los valores iniciales del grafo
    for i in range(num_nodos):
        for j in range(num_nodos):
            if graph[i][j] != float('inf'):
                distancias[i][j] = graph[i][j]

    # Algoritmo de Floyd-Warshall
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias


# Ejemplo de uso:
# Supongamos un grafo con 4 nodos, donde la ausencia de arista se representa con float('inf')
grafo_ejemplo = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

resultados = floyd_warshall(grafo_ejemplo)
for fila in resultados:
    print(fila)
