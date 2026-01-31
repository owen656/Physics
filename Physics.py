import pygame
import Object

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class PhysicsObjectError(Exception):
     def __init__(self, message:str):
        super().__init__(message)
        self.message = message

running = True

Object.add_object()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise PhysicsObjectError("User tried to QUIT")
    

    screen.fill((255,255,255))
    Object.update(screen)

    clock.tick(90)
    pygame.display.flip()