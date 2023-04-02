from pygame import *

BG_color = (0, 0, 0,)
WIDTH, HEIGHT = 800, 600
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping-Pong")
mw.fill(BG_color)
clock = time.Clock()

run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)