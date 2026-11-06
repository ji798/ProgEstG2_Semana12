grafo = {
    "Managua": ["León", "Granada", "Masaya"],
    "León": ["Managua", "Estelí"],
    "Estelí": ["León"],#Actividad 2: Se añade Esteli conectado a León en ambos sentidos, si solo se añade Estelí en la lista de León,
                       # no se puede acceder a León desde Estelí.
    "Granada": ["Managua", "Masaya"],
    "Masaya": ["Managua", "Granada"]
}


def mostrar_grafo(conexiones):
    for vertice, vecinos in conexiones.items():
        print(vertice, "->", ", ".join(vecinos))



mostrar_grafo(grafo)

vertices = ["A", "B", "C", "D"]
matriz = [
    [0, 1, 1, 0],#actividad 3: Las casillas 1-3 y 3-1 demuestran que A y C están conectados
                 #para añadir a la matriz una conexión entre A y D, se debe cambiar la casilla 1-4 y 4-1 de 0 a 1
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

"""
Actividad 4
Con el ejemplo 3, crea el vértice Masaya, conéctalo con Granada y comprueba mediante una función 
si existe conexión directa entre Masaya y Managua. Explica la diferencia entre conexión directa 
y camino con vértices intermedios."""

#La diferencia entre conexion directa y camino con vertices intermedios
#es que la conexion directa es cuando dos vertices estan conectados entre 
#si sin necesidad de pasar por otro vertice, mientras que un camino con vertices 
#intermedios es cuando para llegar de un vertice a otro se debe pasar por uno o mas vertices y aristas intermedios.

def mostrar_matriz(nodos, conexiones):
    print("   ", " ".join(nodos))
    for i in range(len(nodos)):
        print(nodos[i], " ", " ".join(map(str, conexiones[i])))


mostrar_matriz(vertices, matriz)


def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        return True
    return False


def agregar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return False
    if destino in grafo[origen]:
        return False

    grafo[origen].append(destino)
    grafo[destino].append(origen)
    return True


def consultar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return None
    return grafo[vertice][:]


def existe_arista(grafo, origen, destino):
    return origen in grafo and destino in grafo[origen]


def mostrar_grafo(grafo):
    for vertice, vecinos in grafo.items():
        print(vertice, "->", vecinos)


grafo = {}
for ciudad in ["Managua", "León", "Granada"]:
    agregar_vertice(grafo, ciudad)

agregar_arista(grafo, "Managua", "León")
agregar_arista(grafo, "Managua", "Granada")
mostrar_grafo(grafo)
print("Vecinos de Managua:", consultar_vecinos(grafo, "Managua"))
print("¿Conexión León-Granada?:", existe_arista(grafo, "León", "Granada"))
agregar_vertice(grafo, "Masaya")#Actividad 4: Se añade el vertice Masaya al grafo, pero no se conecta con ningún otro vertice
agregar_arista(grafo, "Masaya", "Granada")#ACtividad 4: Se conecta Masaya con Granada, pero no con Managua
print("¿Conexión Masaya-Managua?:", existe_arista(grafo, "Masaya", "Managua"))


"""
Actividad 5. Comprobar las eliminaciones
Ejecuta el ejemplo 4. 
Explica por qué al eliminar un vértice también 
se eliminan sus referencias en las listas de sus vecinos. 
Modifica el código para eliminar primero la arista B—C y observa el resultado
"""
#porque, al eliminar el vértice del grafo, es necesario mantener la consistencia de la estructura del grafo. 
#Si no se eliminan las referencias en las listas de los vecinos, esos vecinos seguirían apuntando a un vértice que ya no existe, 
#lo que podría causar errores o comportamientos inesperados al intentar acceder a ese vértice eliminado.


def eliminar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if destino not in grafo[origen]:
        return False

    grafo[origen].remove(destino)
    grafo[destino].remove(origen)
    return True


def eliminar_vertice(grafo, vertice):
    if vertice not in grafo:
        return False

    for vecino in grafo[vertice][:]:
        grafo[vecino].remove(vertice)
    del grafo[vertice]
    return True


grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

eliminar_arista(grafo, "B", "C")
print("Después de eliminar B-C:", grafo)

eliminar_arista(grafo, "A", "B")
print("Después de eliminar A-B:", grafo)
eliminar_vertice(grafo, "C")
print("Después de eliminar C:", grafo)


"""
Actividad 6. Comparar costos conocidos
Añade una ruta directa B—D de costo 9 y una ruta C—D de costo 4 (en ambos sentidos). 
Compara manualmente los costos de A → B → D y A → C → D e indica cuál resulta menor.
"""

rutas = {
    "A": {"B": 12, "C": 20},
    "B": {"A": 12, "C": 7, "D": 9},
    "C": {"A": 20, "B": 7, "D": 4},
    "D": {"B": 9, "C": 4}
}


def costo_directo(grafo, origen, destino):
    if origen not in grafo:
        return None
    return grafo[origen].get(destino)


print("Costo A-C:", costo_directo(rutas, "A", "C"))
print("Costo A-D:", costo_directo(rutas, "A", "D"))
print("Costo de A-B-C:", costo_directo(rutas, "A", "B") +
      costo_directo(rutas, "B", "C"))
print("Costo de A-C-D:", costo_directo(rutas, "A", "C") +
      costo_directo(rutas, "C", "D"))
print("Costo de A-B-D:", costo_directo(rutas, "A", "B") +
      costo_directo(rutas, "B", "D"))


"""Actividad 7. Red de laboratorios universitarios
Una universidad cuenta con cinco laboratorios: Redes, Software, Robótica, Datos y Electrónica. 
Conexiones: Redes—Software, Software—Datos, Software—Robótica, Robótica—Electrónica y Datos—Electrónica. 
Construye un diccionario de adyacencia, muestra las conexiones, agrega un laboratorio Seguridad 
conectado a Redes y consulta sus vecinos. Incluye una función que cuente cuántas conexiones 
directas tiene cada laboratorio.
"""

universidad = {
    "redes": {"software": 12, "datos": 20},
    "software": {"redes": 12, "datos": 7, "robótica": 9},
    "robótica": {"software": 7, "electrónica": 4},
    "datos": {"redes": 20, "electrónica": 4},
    "electrónica": {"robótica": 4, "datos": 4}
}

def contar_conexiones(grafo, vertice):
    if vertice not in grafo:
        return 0
    return len(grafo[vertice])

def agregar_laboratorio(grafo, laboratorio, conexiones):
    if laboratorio not in grafo:
        grafo[laboratorio] = conexiones
        for vecino in conexiones:
            if vecino in grafo:
                grafo[vecino][laboratorio] = conexiones[vecino]
        return True
    return False

def consultar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return None
    return list(grafo[vertice].keys())

mostrar_grafo(universidad)
agregar_laboratorio(universidad, "seguridad", {"redes": 5})
mostrar_grafo(universidad)
print("Vecinos de Seguridad:", consultar_vecinos(universidad, "seguridad"))
print("Conexiones directas de Redes:", contar_conexiones(universidad, "redes"))


"""Actividad 8. Sistema de transporte
Diseña un programa para administrar conexiones entre al menos cinco ciudades.
Debe utilizar funciones para agregar ciudad, conectar dos ciudades, mostrar vecinos,
consultar conexión directa y eliminar una conexión. Presenta la estructura inicial,
dos operaciones realizadas y el resultado final. Explica si tu grafo es dirigido o no dirigido.
"""

def agregar_ciudad_transporte(grafo, ciudad):
    if ciudad in grafo:
        return False
    grafo[ciudad] = []
    return True


def conectar_ciudades(grafo, origen, destino):
    if origen not in grafo or destino not in grafo or origen == destino:
        return False
    if destino in grafo[origen]:
        return False

    grafo[origen].append(destino)
    grafo[destino].append(origen)
    return True


def mostrar_vecinos_ciudad(grafo, ciudad):
    if ciudad not in grafo:
        return None
    return grafo[ciudad][:]


def hay_conexion_directa(grafo, origen, destino):
    return origen in grafo and destino in grafo[origen]


def eliminar_conexion(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if destino not in grafo[origen]:
        return False

    grafo[origen].remove(destino)
    grafo[destino].remove(origen)
    return True


transporte = {}
for ciudad in ["Managua", "León", "Granada", "Masaya", "Estelí"]:
    agregar_ciudad_transporte(transporte, ciudad)

for origen, destino in [
    ("Managua", "León"),
    ("Managua", "Granada"),
    ("León", "Estelí"),
    ("Granada", "Masaya"),
]:
    conectar_ciudades(transporte, origen, destino)

print("\nEstructura inicial del sistema de transporte:")
mostrar_grafo(transporte)

print("\nOperación 1: conectar Managua con Estelí.")
print("Conexión agregada:", conectar_ciudades(transporte, "Managua", "Estelí"))
print("Vecinos de Estelí:", mostrar_vecinos_ciudad(transporte, "Estelí"))
print(
    "¿Hay conexión directa entre Managua y Estelí?:",
    hay_conexion_directa(transporte, "Managua", "Estelí"),
)

print("\nOperación 2: eliminar la conexión Granada-Masaya.")
print("Conexión eliminada:", eliminar_conexion(transporte, "Granada", "Masaya"))

print("\nEstructura final del sistema de transporte:")
mostrar_grafo(transporte)
print(
    "¿Hay conexión directa entre Granada y Masaya?:",
    hay_conexion_directa(transporte, "Granada", "Masaya"),
)
print(
    "El grafo es no dirigido: cada conexión se registra en las listas de ambas ciudades."
)

"""
¿En qué se diferencia un árbol de un grafo? 
 un arbol se diferencia de un grafo en que es una estructura jerárquica sin ciclos, mientras que un grafo puede tener ciclos y no necesariamente tiene una jerarquía.
¿Por qué una conexión no dirigida debe registrarse en ambos sentidos? 
 Para que se pueda acceder a la conexión desde ambos extremos.
¿Cuándo sería útil usar pesos?
 para representar costos o distancias en un mapa o matriz.
"""
