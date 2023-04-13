from pygame import *
from random import randint
from time import sleep
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
font = font.Font(None, 72)
lose1 = font.render("1 lose!", True, (150, 0, 0))
lose2 = font.render("2 lose!", True, (150, 0, 0))
game = True
finish = False
fatalLeft = 0
fatalRight = 0
scoreL = font.render("Score: " + str(fatalRight), True, (0, 160, 0))
scoreR = font.render("Score: " + str(fatalLeft), True, (0, 160, 0))


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

r1 = Player("rect.png", 50, 200, 10, 0, 10)
r2 = Player("rect.png", 50, 200, ww-60, 0, 10)
ball = GameSprite("ball.png", 50, 50, 250, 250, 0)
ball2 = GameSprite("ball.png", 50, 50, 450, 250, 0)
sx = 2
sy = 2
sx2 = 3
sy2 = 3
bits = 0 
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
        ball.rect.x += sx
        ball.rect.y += sy
        ball.move()
        ball2.rect.x += sx2
        ball2.rect.y += sy2
        ball2.move()
        window.blit(scoreL, (10, 10))
        window.blit(scoreR, (ww-220, 10))
        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
            sx *= -randint(700, 1300)/1000
            sy *= randint(500, 1500)/1000
            bits += 1
            if (bits > randint(0, 5)):
                bits = 0
                sx *= 1.33
                sy *= 1.25
        if sprite.collide_rect(r1, ball2) or sprite.collide_rect(r2, ball2):
            sx2 *= -randint(700, 1300)/1000
            sy2 *= randint(500, 1500)/1000
            if (bits > randint(0, 5)):
                bits = 0
                sx2 *= 1.33
                sy2 *= 1.25
        if ball.rect.y >= wh-50 or ball.rect.y <= 0:
            sy *= -randint(500, 1500)/1000
        if ball2.rect.y >= wh-50 or ball2.rect.y <= 0:
            sy2 *= -randint(500, 1500)/1000
        if ball.rect.x <= -10 or ball2.rect.x <= -10:
            fatalLeft += 1
            scoreR = font.render("Score: " + str(fatalLeft), True, (0, 160, 0))
            if fatalRight <= 5:
                sleep(1)
                finish = False
                ball.rect.x = 250
                ball.rect.y = 250
                ball2.rect.x = 450
                ball2.rect.y = 250
            else:
                window.blit(lose1, (ww/2.5, wh/2))
                finish = True
        if ball.rect.x >= ww-40 or ball2.rect.x >= ww-40:
            fatalRight += 1
            scoreL = font.render("Score: " + str(fatalRight), True, (0, 160, 0))
            if fatalRight <= 5:
                sleep(1)
                finish = False
                ball.rect.x = 250
                ball.rect.y = 250
                ball2.rect.x = 450
                ball2.rect.y = 250
            else:
                window.blit(lose2, (ww/2.5, wh/2))
                finish = True
        display.update()
        clock.tick(FPS)
        
    
