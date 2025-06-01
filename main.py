# This allows us to use code from the pygame library
import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() # Initializer
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating a new GUI window for game

    updatable = pygame.sprite.Group()
    drawbable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawbable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Creating a player instance

    Asteroid.containers = (asteroids, updatable, drawbable)
    AsteroidField.containers = updatable
    asteroidField = AsteroidField()

    while True: # Infinite game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit criteria

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()

        pygame.Surface.fill(screen, (0,0,0))
        
        for object in drawbable:
            object.draw(screen)

        pygame.display.flip()
        
        # Limiting framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()