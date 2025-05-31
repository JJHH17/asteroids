# This allows us to use code from the pygame library
import pygame
from constants import *
from player import Player

def main():
    pygame.init() # Initializer

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating a new GUI window for game
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Creating a player instance
    while True: # Infinite game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit criteria

        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        # Limiting framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()