from lib import Renderer, color, V3, V2

width = 960
height = 540

rend = Renderer(width, height)

rend.glLoadModel("catmodel.obj",
                 translate=V3(width/2, height/4, 0),
                 #  rotate=V3(0, 180, 45),
                 scale=V3(10, 10, 10))

rend.glFinish("output.bmp")
