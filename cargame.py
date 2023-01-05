import pygame
from sys import exit
import random
pygame.init()

green=(0,255,0)
screen=pygame.display.set_mode((600,900))
pygame.display.set_caption("Car Game")
screen.fill(green)
car1=pygame.image.load("car/car1.png")
car11=pygame.image.load("car/car11.png")
car12=pygame.image.load("car/car12.png")
car13=pygame.image.load("car/car13.png")
car14=pygame.image.load("car/car14.png")
car15=pygame.image.load("car/car15.png")
car16=pygame.image.load("car/car16.png")
car2=pygame.image.load("car/car2.png")

x1=170
x2=340
y1=0
y2=650
car=car11
r=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
            elif event.key==pygame.K_RIGHT:
                x2 = 340
            elif event.key==pygame.K_LEFT:
                x2 = 170
    
    y1=y1+2
    if y1==940:
        y1=0
        if random.randint(0,1)==0:
            x1=170
        else:
            x1=340
        r=random.randrange(0,7)
        if r==0:car=car1
        elif r==1:car=car11
        elif r==2:car=car12
        elif r==3:car=car13
        elif r==5:car=car14
        elif r==6:car=car15
        else:car=car16

    if x1==x2 and y1+180==y2:
        pygame.quit()

    pygame.draw.rect(screen,(0,0,0),(110,0,375,900))
    pygame.draw.line(screen,(255,255,255),(300,0),(300,900),10)
    pygame.draw.line(screen,(255,255,255),(130,0),(130,900),5)
    pygame.draw.line(screen,(255,255,255),(465,0),(465,900),5)
    screen.blit(car,(x1,y1))
    screen.blit(car2,(x2,y2))

    pygame.display.update()
