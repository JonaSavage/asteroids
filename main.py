import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from constants import *
from player import Player
import pygame

# WSL filepath: boot-dev_projects/github.com/JonaSavage/asteroids

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0)

    print("\nStarting Asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

        # Framerate = 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()