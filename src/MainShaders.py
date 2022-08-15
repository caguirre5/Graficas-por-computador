from lib import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad

width = 540
height = 540

rend = Renderer(width, height)

rend.glClearColor(1, 1, 1)
rend.glClear()
rend.active_shader = flat
rend.active_texture = Texture("src/models/ToonTeddy.bmp")

rend.glLoadModel("src/models/bear.obj",
                 translate=V3(235, height/5, 0),
                 rotate=V3(0, 270, 0),
                 scale=V3(200, 200, 200))

rend.glFinish("output.bmp")
