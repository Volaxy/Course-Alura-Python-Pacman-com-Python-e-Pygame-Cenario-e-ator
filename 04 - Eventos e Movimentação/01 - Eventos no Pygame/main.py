"""
Event Queue
    The "event" module keeps a queue with all the events that occurred in the last moment.
    This queue can be accessed through the "get()" method.
    When the "get()" method is executed the queue is emptied
"""

import pygame

from pacman import Pacman

BLACK = (0, 0, 0)


def __main__():
    pygame.init()

    window = pygame.display.set_mode((800, 600), 0)
    pacman = Pacman()

    while True:
        # Game Rules
        pacman.calculate_rules()

        # Objects
        window.fill(BLACK)
        pacman.paint(window)
        pygame.display.update()

        pygame.time.delay(100)

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    __main__()
