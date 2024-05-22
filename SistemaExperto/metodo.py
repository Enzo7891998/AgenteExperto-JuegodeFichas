import heapq  # Para utilizar la cola de prioridad en el algoritmo A*
import time

def resolver_problema(tablero, limite_movimientos, app):
    movimientos_roja = ['arriba', 'abajo', 'izquierda', 'derecha']
    movimientos_amarilla = ['arriba', 'abajo']
    turno = 'roja'
    visitados = set()
    camino = []
    contador_movimientos = 0
    ultimo_movimiento_roja = None
    ultimo_movimiento_amarilla = None

    # A* para la ficha roja
    def a_star_search(inicio, meta):
        open_set = []
        heapq.heappush(open_set, (0, inicio))
        came_from = {}
        g_score = {inicio: 0}
        f_score = {inicio: calcular_distancia(inicio, meta)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == meta:
                return reconstruir_camino(came_from, current)

            for movimiento in movimientos_roja:
                neighbor = mover_ficha_simulada(tablero, current, movimiento)
                if neighbor == tablero.ficha_amarilla:
                    continue
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + calcular_distancia(neighbor, meta)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    def reconstruir_camino(came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

    def obtener_direccion(movimiento):
        direcciones = {
            'arriba': (-1, 0),
            'abajo': (1, 0),
            'izquierda': (0, -1),
            'derecha': (0, 1)
        }
        for direccion, (dx, dy) in direcciones.items():
            if movimiento == (dx, dy):
                return direccion
        return ""

    while not tablero.es_estado_final() and contador_movimientos < limite_movimientos:
        ficha_roja = tablero.ficha_roja
        ficha_amarilla = tablero.ficha_amarilla

        if turno == 'roja':
            path = a_star_search(ficha_roja, tablero.salida)
            if path:
                siguiente_movimiento = path[1]  # El siguiente paso en el camino
                direccion = obtener_direccion((siguiente_movimiento[0] - ficha_roja[0], siguiente_movimiento[1] - ficha_roja[1]))
                print(f"Turno de la ficha roja: se mueve {direccion}")
                ficha_roja = siguiente_movimiento
                tablero.ficha_roja = ficha_roja
                camino.append(direccion)
                app.mostrar_tablero()
                time.sleep(0.5)
                contador_movimientos += 1
            turno = 'amarilla'
        else:
            mejor_movimiento = None
            menor_distancia = float('inf')
            for movimiento in movimientos_amarilla:
                nueva_pos = mover_ficha_simulada(tablero, ficha_amarilla, movimiento)
                if nueva_pos != ficha_roja and nueva_pos != ficha_amarilla:
                    distancia = calcular_distancia(nueva_pos, ficha_roja)
                    if distancia < menor_distancia:
                        menor_distancia = distancia
                        mejor_movimiento = movimiento

            if mejor_movimiento:
                direccion = obtener_direccion((mover_ficha_simulada(tablero, ficha_amarilla, mejor_movimiento)[0] - ficha_amarilla[0], mover_ficha_simulada(tablero, ficha_amarilla, mejor_movimiento)[1] - ficha_amarilla[1]))
                print(f"Turno de la ficha amarilla: se mueve {direccion}")
                ficha_amarilla = tablero.mover_ficha_amarilla(mejor_movimiento)
                ultimo_movimiento_amarilla = mejor_movimiento
            else:
                # Si no se encontró un movimiento óptimo, hacer un movimiento cualquiera
                for movimiento in movimientos_amarilla:
                    nueva_pos = mover_ficha_simulada(tablero, ficha_amarilla, movimiento)
                    if nueva_pos != ficha_roja:
                        direccion = obtener_direccion((nueva_pos[0] - ficha_amarilla[0], nueva_pos[1] - ficha_amarilla[1]))
                        print(f"Turno de la ficha amarilla: se mueve {direccion}")
                        ficha_amarilla = tablero.mover_ficha_amarilla(movimiento)
                        ultimo_movimiento_amarilla = movimiento
                        break

            app.mostrar_tablero()
            time.sleep(0.5)
            turno = 'roja'

    if tablero.es_estado_final():
        print("¡Problema resuelto!")
        print("Camino:", camino)
        return camino
    else:
        print("No se pudo resolver el problema o se alcanzó el límite de movimientos")
        return None

def mover_ficha_simulada(tablero, ficha, direccion):
    x, y = ficha
    if direccion == 'arriba' and x > 0:
        return (x - 1, y)
    elif direccion == 'abajo' and x < tablero.filas - 1:
        return (x + 1, y)
    elif direccion == 'izquierda' and y > 0:
        return (x, y - 1)
    elif direccion == 'derecha' and y < tablero.columnas - 1:
        return (x, y + 1)
    return ficha

def calcular_distancia(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
