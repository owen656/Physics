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
        self.image = pygame.Surface((radius*2,radius*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.whileloopcrashpreventer = 0

    def update(self,screen):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.x,self.rect.y = self.x, self.y
        self.xspeed *= friction
        self.yspeed *= friction
        self.xspeed *= 0.99
        self.yspeed *= 0.97

        if self.xspeed == 0 and self.yspeed == 0:
            if self.rect.bottom >= self.screen_height - 1:
                self.yspeed += gravity * air_resistance * self.radius *  math.pi / 15
                self.xspeed += random.uniform(-1,1)

        if self.rect.left <= 0:
            self.rect.left = 0
            self.xspeed = -self.xspeed * bounciness * random.uniform(1-randomness, 1+randomness)
        elif self.rect.right >= self.screen_length:
            self.rect.right = self.screen_length
            self.xspeed = -self.xspeed * bounciness * random.uniform(1-randomness, 1+randomness)
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.yspeed = -self.yspeed * bounciness * random.uniform(1-randomness, 1+randomness)
        elif self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
            self.yspeed = -self.yspeed * bounciness * random.uniform(1-randomness, 1+randomness)
        else:
            self.yspeed += gravity * air_resistance * self.radius *  math.pi / 15

        if self.xspeed < 0.5 and self.xspeed > -0.5:
            self.xspeed = 0
        if self.yspeed < 0.5 and self.yspeed > -0.5:
            self.yspeed = 0
        
        for _object in objects:
            if _object != self:
                if pygame.sprite.collide_circle(self,_object):
                    self.xspeed = -self.xspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*friction
                    self.yspeed = -self.yspeed*friction*(bounciness)*random.uniform(1-randomness,1+randomness)*friction
                    self.whileloopcrashpreventer = 0
                    while pygame.sprite.collide_circle(self,_object):
                        self.x += self.xspeed/10
                        self.y += self.yspeed/10
                        self.rect.x,self.rect.y = self.x, self.y
                        self.whileloopcrashpreventer += 1
                        if self.whileloopcrashpreventer > 200:
                            print("Physics.PhysicsObjectError: While loop crash preventer activated in collision detection.")
                            break
                    
        pygame.draw.circle(screen, (255,0,0), (int(self.rect.x),int(self.rect.y)), self.radius)

objects = pygame.sprite.Group()

def add_object(position=(300,300),radius=30,xspeed=5,yspeed=0):
    objects.add(Sphere(position,radius=radius,xspeed=xspeed,yspeed=yspeed))

def update(screen):
    objects.update(screen)
