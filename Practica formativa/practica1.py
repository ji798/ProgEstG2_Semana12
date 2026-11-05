grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

def mostrar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return []
    return grafo[vertice]

print(mostrar_vecinos(grafo, "C"))

def contar_vertices(grafo):
    return len(grafo)

def contar_aristas(grafo):
    count = 0
    for key in grafo:
        count += len(grafo[key])
    return count // 2

print(contar_vertices(grafo))
print(contar_aristas(grafo))

def estan_conectados(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return "No existen los vertices en el grafo"

    if origen == destino:
        return "no pueden ser el mismo vertice"

    if destino in grafo[origen]:
        return True

    return False

def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        return True
    return False

def agregar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return "No existen los vertices en el grafo"

    if destino not in grafo[origen]:
        grafo[origen].append(destino)
        grafo[destino].append(origen)
        return True
    return False

def recorrido_amplitud(grafo, inicio):
    if inicio not in grafo:
        return "El vertice no existe en el grafo"

    visitados = []
    cola = [inicio]
    resultado = []

    while cola:
        vertice = cola.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)
            resultado.append(vertice)
            cola.extend([vecino for vecino in grafo[vertice] if vecino not in visitados])

    return resultado

def existe_ruta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False

    

    visitados = []
    cola = [origen]

    while cola:
        vertice = cola.pop(0)
        if vertice == destino:
            return True
        if vertice not in visitados:
            visitados.append(vertice)
            cola.extend([vecino for vecino in grafo[vertice] if vecino not in visitados])

    return False

print(estan_conectados(grafo, "A", "B"))
print(estan_conectados(grafo, "A", "F"))
print(estan_conectados(grafo, "X", "A"))


agregar_vertice(grafo, "G")
agregar_arista(grafo, "F", "G")
print(grafo["F"])
print(grafo["G"])

print(recorrido_amplitud(grafo, "A"))

print(existe_ruta(grafo, "A", "F"))
print(existe_ruta(grafo, "A", "A"))
print(existe_ruta(grafo, "A", "X"))