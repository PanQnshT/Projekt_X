import pygame
from pygame.math import Vector2

class Ship(object):

    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size()
        self.speed = 1.5
        self.opor = 0.85
        self.gravity = 0.5

        self.pos = Vector2(size[0]/2,(size[1]/2)-(size[1]/4))
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_DOWN]:
            self.add_force(Vector2(0,self.speed))
        if pressed[pygame.K_RIGHT]:
            self.add_force(Vector2(self.speed,0))
        if pressed[pygame.K_LEFT]:
            self.add_force(Vector2(-self.speed,0))

        # Physics
        self.vel *= self.opor
        self.vel -= Vector2(0, -self.gravity)
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        pygame.draw.rect(self.game.screen, (50, 100, 200), pygame.Rect(self.pos.x, self.pos.y, 25, 25))