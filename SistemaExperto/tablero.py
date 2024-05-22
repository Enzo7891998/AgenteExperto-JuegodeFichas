# tablero.py

class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grid = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.ficha_roja = (0, 0)
        self.ficha_amarilla = (filas // 2, columnas // 2)
        self.salida = (filas - 1, columnas - 1)

    def configurar_ficha_roja(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.ficha_roja = (fila, columna)
        else:
            raise ValueError("Posición fuera de los límites del tablero")

    def configurar_ficha_amarilla(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.ficha_amarilla = (fila, columna)
        else:
            raise ValueError("Posición fuera de los límites del tablero")

    def configurar_salida(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.salida = (fila, columna)
        else:
            raise ValueError("Posición fuera de los límites del tablero")

    def mover_ficha_roja(self, direccion):
        x, y = self.ficha_roja
        if direccion == 'arriba' and x > 0:
            self.ficha_roja = (x - 1, y)
        elif direccion == 'abajo' and x < self.filas - 1:
            self.ficha_roja = (x + 1, y)
        elif direccion == 'izquierda' and y > 0:
            self.ficha_roja = (x, y - 1)
        elif direccion == 'derecha' and y < self.columnas - 1:
            self.ficha_roja = (x, y + 1)
        return self.ficha_roja

    def mover_ficha_amarilla(self, direccion):
        x, y = self.ficha_amarilla
        if direccion == 'arriba' and x > 0:
            self.ficha_amarilla = (x - 1, y)
        elif direccion == 'abajo' and x < self.filas - 1:
            self.ficha_amarilla = (x + 1, y)
        elif direccion == 'izquierda' and y > 0:
            self.ficha_amarilla = (x, y - 1)
        elif direccion == 'derecha' and y < self.columnas - 1:
            self.ficha_amarilla = (x, y + 1)
        return self.ficha_amarilla
    
    def estado_actual(self):
        return {
            'ficha_roja': self.ficha_roja,
            'ficha_amarilla': self.ficha_amarilla,
            'salida': self.salida
        }

    def es_estado_final(self):
        return self.ficha_roja == self.salida

    def imprimir_tablero(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) == self.ficha_roja:
                    print('R', end=' ')
                elif (i, j) == self.ficha_amarilla:
                    print('A', end=' ')
                elif (i, j) == self.salida:
                    print('S', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()
