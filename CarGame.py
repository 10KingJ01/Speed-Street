import pygame
from pygame.locals import *
import os

os.system("cls")

version = ("1.0.0")

print("==**= Speed Street =**==\nBy Voyger Video")
print(f"Version {version}")
cartype = ("r")

pygame.init()
screen = pygame.display.set_mode([1024,1024])
pygame.display.set_caption(f"Speed Street - V{version}")
class Background():
    def __init__(self):
        self.bgimage = pygame.image.load("conts/potholeroad.png")
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 228

        self.bgY2 = self.rectBGimg.height
        self.bgX2 = 228

        self.moving_speed = 5

    def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height

    def render(self):
            screen.blit(self.bgimage, (self.bgX1, self.bgY1))
            screen.blit(self.bgimage, (self.bgX2, self.bgY2))

back_ground = Background()
keys = [False, False, False, False]
playerpos=[512,100]
player = pygame.image.load(f"conts/{cartype}.png")
screen.fill((225,225,225))

Running = True
Intro = True

while Intro:
    pygame.font.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Intro = False
    
    screen.fill(0)
    screen.fill((225, 225, 225))
    largeText = pygame.font.Font("conts/oswald.ttf",150)
    textSurf = largeText.render("Speed Street", False, (0, 0, 0))
    smallText = pygame.font.Font("conts/oswald.ttf",75)
    textSurfsmall = smallText.render("Press space to continue", False, (0, 0, 0))
    screen.blit(textSurf,(0,0))
    screen.blit(textSurfsmall,(0,175))
    pygame.display.update()

while Running:
    screen.fill(0)
    screen.fill((0, 145, 29))
    
    back_ground.update()
    back_ground.render()
    screen.blit(player, playerpos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:

            if event.key==K_a:
                surfacecolour = screen.get_at((playerpos))
                keys[1]=True
                surfacecolour = (f"{surfacecolour}")
                if surfacecolour in ("(0, 145, 29, 255)", "(255, 139, 55, 255)", "(230, 230, 232, 255)", "(178, 178, 178, 225)", "(255, 137, 51, 255)"):
                    Running = False
            
            elif event.key==K_d:
                surfacecolour = screen.get_at((playerpos))
                keys[3]=True
                surfacecolour = (f"{surfacecolour}")
                if surfacecolour in ("(0, 145, 29, 255)", "(255, 139, 55, 255)", "(230, 230, 232, 255)", "(178, 178, 178, 225)", "(255, 137, 51, 255)"):
                    Running = False

            elif event.key==K_b:
                surfacecolour = screen.get_at((playerpos))
                surfacecolour = (f"{surfacecolour}")
                print(f"Surface colour is {surfacecolour}")
                if surfacecolour in ("(0, 145, 29, 255)", "(255, 139, 55, 255)", "(230, 230, 232, 255)", "(178, 178, 178, 225)", "(255, 137, 51, 255)"):
                    Running = False

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_a:
                surfacecolour = screen.get_at((playerpos))
                surfacecolour = (f"{surfacecolour}")
                if surfacecolour in ("(0, 145, 29, 255)", "(255, 139, 55, 255)", "(230, 230, 232, 255)", "(178, 178, 178, 225)", "(255, 137, 51, 255)"):
                    Running = False
                keys[1]=False
            elif event.key==pygame.K_d:
                surfacecolour = screen.get_at((playerpos))
                surfacecolour = (f"{surfacecolour}")
                if surfacecolour in ("(0, 145, 29, 255)", "(255, 139, 55, 255)", "(230, 230, 232, 255)", "(178, 178, 178, 225)", "(255, 137, 51, 255)"):
                    Running = False
                keys[3]=False
            elif event.key == pygame.K_LEFT:
                keys[1]=False
            elif event.key == pygame.K_RIGHT:
                keys[3]=False
            elif event.key == pygame.K_BACKSPACE:
                Running = False

    if keys[0]:
        playerpos[1]-=2
    elif keys[2]:
        playerpos[1]+=2
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    
    pygame.display.flip()

os.system("cls")
print("== GAME OVER ==")
print("Thanks for playing!")