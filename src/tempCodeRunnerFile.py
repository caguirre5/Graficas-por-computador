m = -0.5
b = height / 2

for x in range(width):
    y = int(m * x + b)
    rend.glPoint(x, y)