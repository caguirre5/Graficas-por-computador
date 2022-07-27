from lib import Renderer, color, V3
import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("model.obj",
                 translate = V3(width/2, height/2, 0),
                 scale = V3(450,300,1) )


rend.glFinish("output.bmp")