from lib import Renderer, color, V2
import random

width = 200
height = 200

rend = Renderer(width, height)

rend.glTriangle2(V2(10, 10), V2(100, 190), V2(190, 10))

rend.glFinish('Barycentric.bmp')