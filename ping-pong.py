from pygame import *
from random import randint
from time import sleep
from time import time as timer 

window = display.set_mode((700,500))
display.set_caption("a")
clock = time.Clock()
FPS = 60
scoreInt = 0
fatalInt = 0
font.init()


class GameSprite(sprite.Sprite):
    def __init__(self, img, ximg, yimg, x, y, s):
        super().__init__()
        self.image = transform.scale(image.load(img), (ximg, yimg))
        self.s = s
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.s
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.s
    def tapiy(self):
        pyla = Pylka("bullet.png", 30,40, self.rect.centerx, self.rect.y, 3)
        pyli.add(pyla)
        #zvyk_tapiva.play()
class Enemy(GameSprite):
    def update(self):
        global fatalInt
        self.rect.y += self.s
        if self.rect.y >= 460:
            fatalInt = fatalInt + 1
            self.rect.y = 0
            self.rect.x = randint(0, 700)
            self.s = randint(1, 3)
            if self.s == 3:
                self.s /=2