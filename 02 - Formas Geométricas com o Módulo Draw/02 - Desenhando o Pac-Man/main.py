import pygame

from pacman import Pacman


def __main__():
    pygame.init()

    window = pygame.display.set_mode((640, 480), 0)
    pacman = Pacman()

    while True:
        # Game Rules

        # Objects
        pacman.paint(window)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        # Events


if __name__ == "__main__":
    __main__()
