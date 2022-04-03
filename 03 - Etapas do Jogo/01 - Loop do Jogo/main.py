"""
Frames Per Second (FPS)
    You can use pygame's "time" module to force a number of frames per second.

    pygame.time.delay(<milliseconds>)

    Or use the "clock" class
    # Put at startup
    clk = pygame.time.Clock()

    # Put inside the loop
    clk.tick(<frames per second>)
"""

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
