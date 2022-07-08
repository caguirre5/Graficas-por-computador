from lib import Renderer

rend = Renderer(1024, 512)

rend.glClearColor(1,0,0)
rend.glColor(1,1,0)
rend.glClear()

for i in range(512):
    rend.glPoint(i, i)

rend.libFinish("output.bmp")