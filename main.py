# This allows us to use code from the pygame library
import pygame
from constants import *

def main():
    pygame.init() # Initializer
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating a new GUI window for game

    while True: # Infinite game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit criteria
            
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()