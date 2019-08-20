import pygame, random


class fish:
    def __init__(self,pos):
        self.image = pygame.image.load("fish.png")
        scale = random.randint(1,5)*10
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(2,6))

        rotation = random.randint(0, 360)
        self.speed.rotate.ip(rotation)
        self.image = pygame.transform.rotate(self.image, 180 - rotation)