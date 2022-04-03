import pygame

from pacman import Pacman

BLACK = (0, 0, 0)


def __main__():
    pygame.init()

    window = pygame.display.set_mode((640, 480), 0)
    pacman = Pacman()

    while True:
        # Game Rules
        pacman.calculate_rules()

        # Objects
        window.fill(BLACK)
        pacman.paint(window)
        pygame.display.update()

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    __main__()
