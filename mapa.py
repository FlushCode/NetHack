class Mapa(object):
    """Representa al mapa del juego."""

    def __init__(self, ancho, alto):
        """Inicializa un mapa con dimensiones (ancho, alto)"""
        self.celdas = []
        self.actores = []
        for x in xrange(ancho):
            self.celdas.append([])
            for y in xrange(alto):
                self.celdas[x].append(None)

    def ancho(self):
        """Devuelve la cantidad de columnas del mapa."""
        return len(self.celdas)

    def alto(self):
        """Devuelve la cantidad de filas del mapa."""
        return len(self.celdas[0])

    def agregar_actor(self, actor, x, y):
        """Agregar un actor en la posicion (x, y)"""
        self.actores.append(actor)
        self._ocupar_celda(actor, x, y)

    def eliminar_actores_muertos(self):
        """Elimina los actores muertos de la lista de actores, y los devuelve."""
        actores_vivos = []
        for actor in self.actores:
            if actor.esta_vivo():
                actores_vivos.append(actor)
            else:
                self._desocupar_celda(actor)
        self.actores = actores_vivos

    def _ocupar_celda(self, actor, x, y):
        """Posiciona el actor en la posicion (x, y). Lanza una excepcion si la
        posicion ya estaba ocupada por otro actor."""
        if self.celdas[x][y] and self.celdas[x][y].esta_vivo():
            raise Exception("Celda ocupada")
        self.celdas[x][y] = actor
        actor.x = x
        actor.y = y

    def _desocupar_celda(self, actor):
        """Desocupa la celda ocupada por el actor."""
        if self.celdas[actor.x][actor.y] is actor:
            self.celdas[actor.x][actor.y] = None

    def mover_actor(self, actor, x, y):
        """Mueve el actor desde su posicion actual a la posicion (x, y)"""
        self._desocupar_celda(actor)
        self._ocupar_celda(actor, x, y)

    def dibujar(self, ventana):
        """Dibuja el contenido de todas las celdas del mapa en la ventana provista"""
        for x, colunma in enumerate(self.celdas):
            for y, actor in enumerate(colunma):
                caracter = '.'
                if actor:
                    caracter = actor.dibujar()
                ventana.addstr(y, x, caracter)

    def get_celda(self, x, y):
        """Devuelve el actor ocupante de una posicion determinada. En caso de que la
        posicion este vacia, devuelve None. """
        return self.celdas[x][y]

    def posicion_valida(self, x, y):
        """Devuelve si la posicion esta dentro de los limites del mapa."""
        return 0 <= x < self.ancho() and 0 <= y < self.alto()
