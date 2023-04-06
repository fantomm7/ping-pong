from pygame import *
from random import randint
#from time import sleep
#from time import time as timer 

back = (150, 200, 176)
wh = 500
ww = 700
window = display.set_mode((ww, wh))
display.set_caption("ping-pong game")
clock = time.Clock()
window.fill(back)
FPS = 60
font.init()
font = font.Font(None, 25)
lose1 = font.render("1 lose!", True, (150, 0, 0))
lose2 = font.render("2 lose!", True, (150, 0, 0))
game = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, img, ximg, yimg, x, y, s):
        super().__init__()
        self.image = transform.scale(image.load(img), (ximg, yimg))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = s
    def move(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.s
        if keys[K_s] and self.rect.y <= wh-200:
            self.rect.y += self.s
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.s
        if keys[K_DOWN] and self.rect.y <= wh-200:
            self.rect.y += self.s

r1 = Player("rect.png", 100, 200, 75, 0, 5)
r2 = Player("rect.png", 100, 200, ww-175, 0, 5)
ball = GameSprite("ball.png", 50, 50, 350, 250, 3)
sx = 3
sy = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        r1.update_l()
        r2.update_r()
        r1.move()
        r2.move()
        ball.move()
        ball.rect.x += sx
        ball.rect.y += sy
        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
            speed_x *= -1
            sy *= 1
        if ball.rect.y >= wh-50 or ball.rect.y <= 0:
            sy *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x >= ww:
            finish = True
            window.blit(lose2, (200, 200))

        display.update()
        clock.tick(FPS)