import pygame


YELLOW = (255, 255, 0)


def __main__():
    pygame.init()

    # Use the ".set_mode()" informing the screen resolution to create the game screen
    window = pygame.display.set_mode((640, 480), 0)

    # The game consist in 3 parts:
    # 1º) The game rules
    # 2º) Print the objects in the window
    # 3º) Events of the game
    while True:
        # Game Rules

        # Objects
        # The ".draw" draw an object inside the window
        # The circle is draw as follows:
        # 1 - The window that the circle will be drawn, 2 - The color of the circle, 3 - The coordinates that will be
        # drawn the circle, 4 - The range of the circle, 5 - The thickness of the circle
        pygame.draw.circle(window, YELLOW, (320, 240), 50, 5)
        # Update the window with the objects drawn in memory and transfers the drawing to the screen
        pygame.display.update()

        # Events
        # The ".event.get()" receives all the events during the game
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    __main__()
