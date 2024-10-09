import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		pygame.sprite.Sprite.__init__( self, self.containers )
		super().__init__(x, y, radius)
		self.velocity = ( 1, 0 )
	
	def draw(self, screen):
		pygame.draw.circle(screen, "grey", self.position, self.radius, 2 )
	
	def update(self, dt):
		self.position += self.velocity * dt

