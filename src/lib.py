import struct 

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
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

        self.glClear()

    def glClear(self):         #List comprehension: Asigna color a cada posicion
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)

    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor

    def libFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3))) #tama;o del archivo, cantidad de bytes que va a usar en memoria
            file.write(dword(0))
            file.write(dword(14 + 40)) #El byte donde empieza la informacion de pixeles

            # InfoHeader
            file.write(dword(40))
            file.write(dword(self.width)) #Width
            file.write(dword(self.height)) #Height
            file.write(word(1)) #Planes, solo ocupa 2 bytes
            file.write(word(24))#Bits Per Pixel
            file.write(dword(0)) #Compression
            file.write(dword(14 + 40 + (self.width * self.height * 3))) #Tama;o de la imagen
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            
              #Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
