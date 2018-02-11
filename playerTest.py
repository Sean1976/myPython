import pygame
import random

from pygame.locals import *     # 调用 pygame.locals 使容易使用关键参数
# 定义Player对象 调用super赋予它属性和方法
# 我们画在屏幕上的surface 现在是player的一个属性
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf=pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect(center=(400,300))     #player 的初始位置
    def update(self,pressed_keys):
       if pressed_keys[K_UP]:
          self.rect.move_ip(0,-5)
       if pressed_keys[K_DOWN]:
          self.rect.move_ip(0,5)
       if pressed_keys[K_LEFT]:
          self.rect.move_ip(-5,0)
       if pressed_keys[K_RIGHT]:
          self.rect.move_ip(5,0)

       if self.rect.left <= 0:
          self.rect.left = 0
       elif self.rect.right >= 800:
          self.rect.right = 800
       if self.rect.top <= 0:
          self.rect.top = 0
       elif self.rect.top >= 600:
          self.rect.top = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf=pygame.Surface((20,20))
        self.surf.fill((255,255,255))
        self.rect=self.surf.get_rect(center=(random.randint(820,900),random.randint(0,600)))
        self.speed=random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<=0:
           self.kill

pygame.init()

# 创建屏幕对象
# 设定尺寸为 800x600
screen=pygame.display.set_mode((800,600))
#为添加敌人创建自定义事件
ADDENEMY=pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY,1000)

player=Player()                   # 初始化Player， 现在他仅仅是一个矩形
background=pygame.Surface(screen.get_size())
background.fill((0,0,0))

enemies=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)

running=True
while running:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:    #按下Esc  键时触发
                running=False
        elif event.type==QUIT:        #鼠标直接关闭窗口时触发
            running=False
        elif(event.type==ADDENEMY):
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        screen.blit(background,(0,0))          #矩形方格之外的背景色要重新刷新，可以去掉这句看看效果，好像和下面这句效果一样，暂且不知道有什么区别
        # screen.fill((0,0,0))                  #矩形方格之外的背景色要重新刷新，可以去掉这句看看效果
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        for entity in all_sprites:
            screen.blit(entity.surf,entity.rect)             #将surf画到最新的坐标上
        if pygame.sprite.spritecollideany(player,enemies):
            player.kill()
        #screen.blit(player.surf,player.rect)  # 这一行表示：将surf画到最新的坐标上
        pygame.display.flip()               #刷新屏幕

