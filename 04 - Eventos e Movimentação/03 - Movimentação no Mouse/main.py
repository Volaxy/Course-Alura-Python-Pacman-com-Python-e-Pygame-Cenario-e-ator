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

        pygame.time.delay(50)

        # Events
        events = pygame.event.get()
        pacman.process_mouse_events(events)


if __name__ == "__main__":
    __main__()
