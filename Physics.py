from __future__ import annotations
import pygame
import Object
import random

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class PhysicsObjectError(Exception):
     def __init__(self, message:str):
        super().__init__(message)
        self.message = message

running = True
for i in range(15):
    Object.add_object(position=(random.randint(0,600),random.randint(0,600)),radius=20,xspeed=10,yspeed=0)
Object.add_object(position=(300,100),radius=30,xspeed=0,yspeed=0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise PhysicsObjectError("User tried to QUIT")

    screen.fill((255,255,255))
    for i in range(1):
        Object.update(screen)

    clock.tick(90)
    pygame.display.flip()