import pygame


BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

SPEED = 1
RADIUS = 30


def __main__():
    pygame.init()

    window = pygame.display.set_mode((640, 480), 0)

    x = 10
    y = 10
    speed_x = SPEED
    speed_y = SPEED
    while True:
        # Game Rules
        x += speed_x
        y += speed_y
        if x + RADIUS > 640:
            speed_x = -SPEED
        if x - RADIUS < 10:
            speed_x = SPEED
        if y + RADIUS > 480:
            speed_y = -SPEED
        if y - RADIUS < 10:
            speed_y = SPEED

        # Objects
        window.fill(BLACK)
        pygame.draw.circle(window, YELLOW, (x, y), RADIUS, 5)
        pygame.display.update()

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    __main__()
