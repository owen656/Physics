from __future__ import annotations
if __name__ == "__main__":
    print("This is Object.py, please run Physics.py")

import pygame
import Physics

gravity = 0.8
friction = 0.9

class Sphere(pygame.sprite.Sprite):
    def __init__(self,position,radius,xspeed,yspeed):
        super().__init__()
        self.x,self.y  = position
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.image = pygame.Surface((self.x,self.y), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()

    def update(self,screen):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.x = self.x
        self.rect.y = self.y
        self.xspeed *= friction
        self.yspeed *= friction

        if self.rect.bottom > self.screen_height:
            self.yspeed = -self.yspeed*friction
        elif self.rect.top < 0:
            self.yspeed = -self.yspeed*friction
        elif self.rect.left < 0:
            self.xspeed = -self.xspeed*friction
        elif self.rect.left > self.screen_length:
            self.xspeed = -self.xspeed*friction
        else:
            self.yspeed += gravity

        if self.xspeed < 0.75 and self.xspeed > -0.75:
            self.xspeed = 0
        if self.yspeed < 0.75 and self.yspeed > -0.75:
            self.yspeed = 0
        
        pygame.draw.circle(screen, (255,0,0), (int(self.x),int(self.y)), self.radius)

objects = pygame.sprite.Group()

def add_object():
    objects.add(Sphere((200,200),50,5,0))

def update(screen):
    objects.update(screen)