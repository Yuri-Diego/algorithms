# implementacao do algoritmo de Dijkstra de acordo com o exemplo do livro
# Entendendo Algoritmos

grafo = {}

grafo["inicio"] = {}

grafo["inicio"]["A"] = 6
grafo["inicio"]["B"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

#DIJKSTRA
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo<custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

# Mostra o custo final mínimo para cada nó
print("Custos finais:", custos)

# Reconstrói o caminho mais curto até o nó "fim"
caminho = []
nodo = "fim"
while nodo is not None:
    caminho.insert(0, nodo)
    nodo = pais.get(nodo)  # Usa get para evitar erros se o nó não tiver um pai

print("Caminho mais curto:", " -> ".join(caminho))