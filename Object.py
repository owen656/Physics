from __future__ import annotations
if __name__ == "__main__":
    print("This is Object.py, please run Physics.py")

import pygame

class Sphere(pygame.sprite.Sprite):
    def __init__(self,position,radius,xspeed,yspeed):
        super().__init__()
        self.x,self.y  = position
        self.radius = radius
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.image = pygame.Surface((self.x,self.y), pygame.SRCALPHA)
    
    def update(self):
        pass
        
objects = pygame.sprite.Group()

def add_object():
    objects.add(Sphere((0,0),50,0,0))