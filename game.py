from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, width, height)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed

class Face(GameSprite):
    def __init__(self,sprite_image,x=0,y=0,width=0,height=0, speed=5):
        super().__init__(sprite_image, x, y, width, height)
        self.dx = speed
        self.dy = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy

    def player_collide(self, Player):
        if sprite.collide_rect(self, Player):
            self.dx *= -1

BG_COLOR = (10, 10, 10)
WIDTH, HEIGHT = 600, 480
FPS = 60

plat1 = Player('plat.png', 10, 200, 30, 90, 5, K_w, K_s)
plat2 = Player('plat.png', 560, 200, 30, 90, 5, K_UP, K_DOWN)
face = Face('face.png', WIDTH//2, HEIGHT//4, 32, 32, 3)


mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-Pong')
mw.fill(BG_COLOR)
clock = time.Clock()

run = True
while run:
    mw.fill(BG_COLOR)
    plat1.update()
    plat2.update()
    plat1.reset()
    plat2.reset()
    face.update()
    face.player_collide(plat1)
    face.player_collide(plat2)
    face.reset()


    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()
    clock.tick(FPS)
