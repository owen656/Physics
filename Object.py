from __future__ import annotations
if __name__ == "__main__":
    print("This is Object.py, please run Physics.py")

import pygame

gravity = 0.8
friction = 0.8

class Sphere(pygame.sprite.Sprite):
    def __init__(self,position,radius,xspeed,yspeed):
        super().__init__()
        self.x,self.y  = position
        self.radius = radius
        self.xspeed2 = xspeed
        self.yspeed2 = yspeed
        self.image = pygame.Surface((self.x,self.y), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.screen_length = self.screen.get_width()
        self.screen_height = self.screen.get_height()

    def update(self,screen):
        self.x += self.xspeed2
        self.y += self.yspeed2
        self.rect.x = self.x
        self.rect.y = self.y

        self.yspeed2 += gravity

        if self.rect.bottom > self.screen_height:
            self.yspeed2 = -self.yspeed2
        if self.rect.top < 0:
            self.yspeed2 = -self.yspeed2
        if self.rect.left < 0:
            self.xspeed2 = -self.xspeed2
        if self.rect.left > self.screen_length:
            self.xspeed2 = -self.xspeed2
        pygame.draw.circle(screen, (255,0,0), (int(self.x),int(self.y)), self.radius)

objects = pygame.sprite.Group()

def add_object():
    objects.add(Sphere((200,200),50,0,0))

def update(screen):
    objects.update(screen)