class Ventana:
    __titulo = None
    __VSIx = None
    __VSIy = None
    __VIDx = None
    __VIDy = None
    def __init__(self, titulo, VSIx=-9999, VSIy=-9999, VIDx=9999, VIDy=9999):
        self.__titulo = titulo
        self.__VSIx = VSIx
        self.__VSIy = VSIy
        self.__VIDx = VIDx
        self.__VIDy = VIDy
    def getTitulo (self):
        return self.__titulo
    def alto (self):
        alto=0
        if self.__VIDy<=500 and self.__VSIy>=0:
            alto = self.__VIDy-self.__VSIy
        return alto
    def ancho (self):
        ancho = 0
        if self.__VIDx<=500 and self.__VSIx>=0:
            ancho = self.__VIDx-self.__VSIx
        return ancho
    def moverDerecha (self, mover=1):
        self.__VSIx += mover
        self.__VIDx += mover
    def moverIzquierda (self, mover=1):
        self.__VSIx -= mover
        self.__VIDx -= mover
    def bajar (self, mover=1):
        self.__VSIy -= mover
        self.__VIDy -= mover
    def subir (self, mover=1):
        self.__VSIy += mover
        self.__VIDy += mover
    def mostrar (self):
        print (self.__titulo)
        if self.__VSIx >= 0:
            print ('Coordenada x del vertice superior izquierdo:', self.__VSIx)
        if self.__VSIy >= 0:
            print ('Coordenada y del vertice superior izquierdo:', self.__VSIy)
        if self.__VIDx <= 500:
            print ('Coordenada x del vertice inferior derecho:', self.__VIDx)
        if self.__VIDy <= 500:
            print ('Coordenada y del vertice inferior derecho:', self.__VIDy)