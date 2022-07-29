from lib import Renderer, color, V3, V2

width = 960
height = 540

rend = Renderer(width, height)

rend.glLoadModel("model.obj",
                 translate=V3(width/2, height/2, 50),
                 rotate = V3(0,180,45),
                 scale=V3(200, 200, 200))

rend.glFinish("output.bmp")
