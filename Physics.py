import pygame
import Object

screen = pygame.display.set_mode((600,600))

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