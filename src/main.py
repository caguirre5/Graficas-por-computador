from lib import Renderer, color, V2
import random

width = 1024
height = 1024
rend = Renderer(width, height)

rend.glClearColor(1,0,0)
rend.glColor(1,1,0)
rend.glClear()

# for x in range(width):
#     for y in range(height):
#         if random.random() < 0.5:
#             rend.glPoint(x,y, color(0,0,0))
#         else:
#             rend.glPoint(x, y, color(1,1,1))

# for x in range(width):
#     for y in range(height):
#         pixelColor = color(random.random(), random.random(), random.random())
#         rend.glPoint(x, y, pixelColor)

# for x in range(width):
#     slope = 1
#     y = slope * x
#     rend.glPoint(x,y)


# -----------------------------------------------------------------------------
#           Renderizacion de espacio con estrellas
# -----------------------------------------------------------------------------

# StarField
# for x in range(width):
#    for y in range(height):
#        if random.random() > 0.999:
#            size = random.randrange(0, 4)
#            brightness = random.random() / 2 + 0.5
#            starColor = color(brightness, brightness, brightness)

#            if size == 0:
#                rend.glPoint(x,y,starColor)
#            if size == 1:
#                rend.glPoint(x,y, starColor)
#                rend.glPoint(x+1,y, starColor)
#                rend.glPoint(x+1,y+1, starColor)
#                rend.glPoint(x,y+1, starColor)
#            if size == 2:
#                rend.glPoint(x,y, starColor)
#                rend.glPoint(x,y+1, starColor)
#                rend.glPoint(x,y-1, starColor)
#                rend.glPoint(x+1,y, starColor)
#                rend.glPoint(x-1,y, starColor)

#            if size == 3:
#                rend.glPoint(x,y, starColor)
#                rend.glPoint(x+1,y, starColor)
#                rend.glPoint(x,y+1, starColor)
#                rend.glPoint(x+1,y+1, starColor)
#                rend.glPoint(x+2,y, starColor)
#                rend.glPoint(x+2,y+1, starColor)
#                rend.glPoint(x,y+2, starColor)
#                rend.glPoint(x+1,y+2, starColor)
#                rend.glPoint(x+2,y+2, starColor)
#                rend.glPoint(x-1,y+1, starColor)
#                rend.glPoint(x+3,y+1, starColor)
#                rend.glPoint(x+1,y-1, starColor)
#                rend.glPoint(x+1,y+3, starColor)
#                rend.glPoint(x-2,y+1, starColor)
#                rend.glPoint(x+4,y+1, starColor)
#                rend.glPoint(x+1,y-2, starColor)
#                rend.glPoint(x+1,y+4, starColor)
#            if size == 4:
#                rend.glPoint(x,y, starColor)
#                rend.glPoint(x+1,y, starColor)
#                rend.glPoint(x,y+1, starColor)
#                rend.glPoint(x+1,y+1, starColor)
#                rend.glPoint(x+2,y, starColor)
#                rend.glPoint(x+2,y+1, starColor)
#                rend.glPoint(x,y+2, starColor)
#                rend.glPoint(x+1,y+2, starColor)
#                rend.glPoint(x+2,y+2, starColor)
#                rend.glPoint(x-1,y+1, starColor)
#                rend.glPoint(x+3,y+1, starColor)
#                rend.glPoint(x+1,y-1, starColor)
#                rend.glPoint(x+1,y+3, starColor)
#                rend.glPoint(x-2,y+1, starColor)
#                rend.glPoint(x+4,y+1, starColor)
#                rend.glPoint(x+1,y-2, starColor)
#                rend.glPoint(x+1,y+4, starColor)
#                rend.glPoint(x-3,y+1, starColor)
#                rend.glPoint(x+5,y+1, starColor)
#                rend.glPoint(x+1,y-3, starColor)
#                rend.glPoint(x+1,y+5, starColor)


# -----------------------------------------------------------------------------
#           Renderizacion de punto dentro de un viewport
# -----------------------------------------------------------------------------

# rend.glViewport(int(width / 4), int(height /4), int(width/2), int(height/2))

# rend.glClearColor(0,1,0)
# rend.glClear()
# rend.glClearViewport(color(1,1,1))

# rend.glPointvp(0,0)


# -----------------------------------------------------------------------------
#               Linea con pendiente
# -----------------------------------------------------------------------------

# m = -0.5
# b = height / 2

# for x in range(width):
#     y = int(m * x + b)
#     rend.glPoint(x, y)

# -----------------------------------------------------------------------------
#               Algoritmo de Bresenham
# -----------------------------------------------------------------------------


rend.glFinish("output.bmp")
