import struct
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=i', d)


def color(b, g, r):
    return bytes(
        [int(b * 255),
         int(g * 255),
         int(r * 255)]
    )


class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.clearColor = color(0, 0, 0)
        self.currColor = color(1, 1, 1)

        self.glViewport(0, 0, self.width, self.height)

        self.glClear()

    def glViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpW = width
        self.vpH = height

    def glClear(self):  # List comprehension: Asigna color a cada posicion
        self.pixels = [[self.clearColor for y in range(
            self.height)] for x in range(self.width)]

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glClearViewport(self, clr=None):
        for x in range(self.vpX, self.vpX + self.vpW):
            for y in range(self.vpY, self.vpY + self.vpH):
                self.glPoint(x, y, clr)

    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor

    def glPointvp(self, ndcx, ndcy, clr=None):
        x = int((ndcx + 1) * (self.vpW / 2) + self.vpX)
        y = int((ndcy + 1) * (self.vpH / 2) + self.vpY)

        self.glPoint(x, y, clr)

    def glLine(self, v0, v1, clr=None):
        # Bresenham line algorithm
        # y = m * x + b
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        # Si el punto0 es igual al punto 1, dibujar solamente un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Si la linea tiene pendiente mayor a 1 o menor a -1
        # intercambio las x por las y, y se dibuja la linea
        # de manera vertical
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si el punto inicial X es mayor que el punto final X,
        # intercambio los puntos para siempre dibujar de
        # izquierda a derecha
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                # Dibujar de manera vertical
                self.glPoint(y, x, clr)
            else:
                # Dibujar de manera horizontal
                self.glPoint(x, y, clr)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1

    def glFill(self, poligono, clr=None):
        for y in range(self.height):
            for x in range(self.width):
                last = len(poligono) - 1
                check = False

                # Este algoritmo verifica los puntos que no estan dentro del poligono
                for i in range(len(poligono)):
                    if (poligono[i][1] < y and poligono[last][1] >= y) or (poligono[last][1] < y and poligono[i][1] >= y):
                        if poligono[i][0] + (y - poligono[i][1]) / (poligono[last][1] - poligono[i][1]) * (poligono[last][0] - poligono[i][0]) < x:
                            check = not check
                    last = i
                if check:
                    self.glPoint(x, y, clr)

    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            # tama;o del archivo, cantidad de bytes que va a usar en memoria
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            # El byte donde empieza la informacion de pixeles
            file.write(dword(14 + 40))

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))  # Width
            file.write(dword(self.height))  # Height
            file.write(word(1))  # Planes, solo ocupa 2 bytes
            file.write(word(24))  # Bits Per Pixel
            file.write(dword(0))  # Compression
            # Tama;o de la imagen
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
