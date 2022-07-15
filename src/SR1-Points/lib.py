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

    def glClear(self):  # List comprehension: Asigna color a cada posicion 20pts
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

    def glLine(self, v0, v1, clr=None):
        # Bresenham line algorithm   y= mx +b

        x0 = int(v0.x)
        x1 = int(v1.y)
        y0 = int(v0.x)
        y1 = int(v1.y)

        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        m = (v1.y - v0.y) / (v1.x-v0.x)
        for x in range(v0.x, v1.x+1):
            y = int(x * m)

            self.glPoint(x, y)
