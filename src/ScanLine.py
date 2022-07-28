from lib import Renderer, color, V2
import random

width = 300
height = 300

rend = Renderer(width, height)

rend.glTriangle(V2(50, 80), V2(50, 160), V2(70, 80))
rend.glTriangle(V2(180, 50), V2(150, 1), V2(70, 50))
rend.glTriangle(V2(180, 150), V2(120, 160), V2(130, 180))

'''
    rend.glModel("model.obj",
                V3())
'''

rend.glFinish('ScanLine.bmp')
