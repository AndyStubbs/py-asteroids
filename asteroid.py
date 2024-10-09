import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		pygame.sprite.Sprite.__init__( self, self.containers )
		super().__init__(x, y, radius)
		self.velocity = ( 1, 0 )
	
	def draw(self, screen):
		pygame.draw.circle(screen, "grey", self.position, self.radius, 2 )
	
	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		split_angle = random.uniform(20, 50)
		rad = self.radius = ASTEROID_MIN_RADIUS
		rock1 = Asteroid(self.position.x, self.position.y, rad)
		rock1.velocity = self.velocity.rotate(split_angle) * 1.2
		rock2 = Asteroid(self.position.x, self.position.y, rad)
		rock2.velocity = self.velocity.rotate(-split_angle) * 1.2



