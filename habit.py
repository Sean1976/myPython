import pygame
import sys
from pygame.locals import *

pygame.init()
size = (width, height) = (1024, 768)
speed=[2, -1]
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("欢迎来到游戏世界")
turtle = pygame.image.load("habit.png")
position = turtle.get_rect()
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            #sys.exit()    #用线程退出也可以
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)   #图形水平翻转
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        #turtle = pygame.transform.flip(turtle, False, True)   #图形垂直翻转
        speed[1] = -speed[1]
    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()
    pygame.time.delay(10)