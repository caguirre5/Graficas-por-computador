# Universidad del Valle de Guatemala
# Cristian Eduardo Aguirre Duarte    20231
# Graficas por Computador

# SR2: Lines ->  Funciones agregadas a la libreria para esta tarea: glLine()

import math
from turtle import position
from lib import Renderer, color, V2
import random


# Preparacion de imagen
width = 1000
height = 1000
rend = Renderer(width, height)

rend.glClearColor(1, 0, 0)
rend.glColor(1, 1, 0)
rend.glClear()

PolygonNumber = 5

# Coordenadas para crear poligonos
pol1 = [V2(640, 520), V2(710, 760), V2(820, 390)]
pol2 = [V2(100, 200), V2(170, 260), V2(260, 170), V2(
    210, 120), V2(210, 170), V2(160, 220), V2(140, 150)]
pol3 = [V2(340, 120), V2(410, 360),  V2(750, 360), V2(520, 90)]
pol4 = [V2(140, 620), V2(210, 760), V2(280, 620)]
pol5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

# Crear poligonos


def GenPolygon(polygon, clr=None):
    for i in range(len(polygon)):
        rend.glLine(polygon[i], polygon[(i + 1) % len(polygon)], clr)


GenPolygon(pol1, color(1, 1, 1))
GenPolygon(pol2, color(1, 1, 1))
GenPolygon(pol3, color(1, 1, 1))
GenPolygon(pol4, color(1, 1, 1))
GenPolygon(pol5, color(1, 1, 1))

rend.glFinish("SR2-Lines.bmp")
