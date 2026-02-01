from __future__ import annotations
import pygame
import Physics
import math
import random

gravity = 1.2
friction = 1
air_resistance = 0.2
bounciness = 0.95
randomness = 0.1

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
        self.rect.x,self.rect.y = self.x, self.y
        self.xspeed *= friction
        self.yspeed *= friction

        self.xspeed *= 0.99
        self.yspeed *= 0.97

        if self.rect.bottom > self.screen_height:
            self.yspeed = -self.yspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*1.1
        elif self.rect.top < 0:
            self.yspeed = -self.yspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*1.1
        elif self.rect.left < 0:
            self.xspeed = -self.xspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*1.1
        elif self.rect.left > self.screen_length:
            self.xspeed = -self.xspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*1.1
        else:
            self.yspeed += gravity * air_resistance * self.radius *  math.pi // 15

        if self.xspeed < 0.5 and self.xspeed > -0.5:
            self.xspeed = 0
        if self.yspeed < 0.5 and self.yspeed > -0.5:
            self.yspeed = 0
        
        pygame.draw.circle(screen, (255,0,0), (int(self.rect.x),int(self.rect.y)), self.radius)

objects = pygame.sprite.Group()

def add_object(position=(300,300),radius=30,xspeed=5,yspeed=0):
    objects.add(Sphere(position,radius=radius,xspeed=xspeed,yspeed=yspeed))

def update(screen):
    objects.update(screen)