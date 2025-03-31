from pygame import *

window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play(-1)
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN',True,(0,255,0))
lose = font.render('YOU LOSE',True,(255,0,0))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class PLayer(GameSprite):
    def update(self):
        keys_pres = key.get_pressed()
        if keys_pres[K_a]and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pres[K_d]and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pres[K_w]and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pres[K_s]and self.rect.y < 435:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <=470:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:
            self.direction ='left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        

    def update2(self):
        if self.rect.y <=170:
            self.direction = 'up'
        if self.rect.y >= 500 - 85:
            self.direction ='down'
        
        if self.direction == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
    
    def update3(self):
    
        if self.rect.x >= 500 - 85: 
            self.direction = 'down'
        if self.rect.y >= 500 - 85:  
            self.direction = 'left'
        if self.rect.x <= 100:  
            self.direction = 'up'
        if self.rect.y <= 170:  
            self.direction = 'right'

        
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        
class Wall(sprite.Sprite):
    def __init__(self,c1,c2,c3,wall_x,wall_y, wall_width,wall_height):
        super().__init__()
        self.image = Surface((wall_width,wall_height))
        self.image.fill((c1,c2,c2))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player = PLayer('hero.png',20,10,3)
monstr = Enemy('cyborg.png',470,250,4)
monstr2 = Enemy('cyborg.png',310,170,3)
gold = GameSprite('treasure.png',550,400,0)


wall1 = Wall(68, 239, 0, 100, 20 , 550, 10)
wall2 = Wall(68, 239, 0, 100, 480, 390, 10)
wall3 = Wall(68, 239, 0, 100, 20 , 10, 380)
wall4 = Wall(68, 239, 0, 200, 110 , 10, 380)
wall5 = Wall(0, 255, 0, 300, 20 , 10, 380)
wall6 = Wall(0, 255, 0, 450, 110 , 10, 380)
walls = [wall1,wall2,wall3,wall4,wall5,wall6]

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
               game = False
    if not finish:
        window.blit(background,(0,0))
        player.reset()
        monstr.reset()
        monstr2.reset()
        gold.reset()
        player.update()
        monstr.update()
        monstr2.update2()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        if sprite.collide_rect(player,gold):
            finish = True
            money.play()
            window.blit(win,(200,200))
        if sprite.collide_rect(player,monstr):
            finish = True
            kick.play()
            window.blit(lose,(200,200))
        if sprite.collide_rect(player,monstr2):
            finish = True
            kick.play()
            window.blit(lose,(200,200))
        for i in walls:
            if sprite.collide_rect(player,i):
                finish = True
                kick.play()
                window.blit(lose,(200,200))
    
    
    time.delay(10)
    display.update()