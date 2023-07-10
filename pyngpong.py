from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y +=  self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y +=  self.speed

class ball(GameSprite):
    def update(self):
        if self.rect.x > 700:
            self.speed *= 3
        elif self.rect.y < 500:
            self.speed *= -3
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

player = Player('download-removebg-preview.png', 5, win_height - 250, 4)
player2 = Player2('download-removebg-preview.png', 640, win_height - 250, 4)
Ball = ball('imad-removebg-preview.png', win_width - 350, 250, 2)
speed = 10 
speed_x = -3
speed_y = -3
game = True
clock = time.Clock()
FPS = 60
x1 = 100
x2 = 150
y1 = 400
y2 = 350 
font.init()
font = font.Font(None, 70)
win = font.render('YOU lose', True, (250, 215, 0))
finish = False
while game:
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.reset()  
        player.update()
        player2.update()        
        player2.reset()
        Ball.update() 
        Ball.reset()  
        if Ball.rect.y >= 450 or Ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(player, Ball):
            speed_x *= -1
        if sprite.collide_rect(player2, Ball):
            speed_x *= -1
    display.update()
    clock.tick(FPS)