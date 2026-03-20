import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}", sep="\n")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
