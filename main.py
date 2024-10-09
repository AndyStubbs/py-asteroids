# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}");
	print(f"Screen height: {SCREEN_HEIGHT}");
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = ( updatable, drawable )
	Asteroid.containers = ( asteroids, updatable, drawable )
	AsteroidField.containers = ( updatable )
	Shot.containers = ( shots, updatable, drawable )
	asteroid_field = AsteroidField()
	for group in Player.containers:
		group.add( player )
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for u in updatable:
			u.update(dt)
		for d in drawable:
			d.draw(screen)
		for a in asteroids:
			if player.check_collision( a ):
				print("Game over!")
				running = False
			for s in shots:
				if s.check_collision( a ):
					a.split()
					s.kill()
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
