"""
Putting Pixels
    It is possible to put pixels on the Surface type object using the "set_at" method.
Syntax:
    <Surface object>.set_at(<position>, <color>)
Example:
    window.set_at((300, 200), (255, 0, 0))


Circles
    It is also possible to draw circles using the "circle" function of the "draw" module, informing the central point
    and the radius in pixels.
Syntax:
    pygame.draw.circle(<Surface>, <Color>, <Center Point>, <radius>, <thickness>)
Example:
    pygame.draw.circle(window, (255, 0, 0), (200, 200), 50, 5)


Rectangles
    Drawing rectangles is also easy using the "rect" function of the "draw" module, needing to inform the upper left
    point, width and height.
Syntax:
    pygame.draw.rect(<Surface>, <color>, <x and y of top left point>, <width>, <thickness>)
Example:
    pygame.draw.rect(window, (255, 0, 0), (100, 100, 200, 200), 5)


polygons
    More complex geometric shapes can be drawn using the "polygon" method of the "draw" module, where it is necessary
    to inform a list of points.
Syntax:
    pygame.draw.rect(<Surface>, <color>, <point list>, <thickness>)
Example of drawing a triangle:
    pygame.draw.polygon(window, (255, 0, 0), [(100, 100), (200, 200), (100, 200)], 5)
"""

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
