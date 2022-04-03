import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Pacman:
    def __init__(self):
        self.center_x = 320
        self.center_y = 240
        self.size = 100
        self.radius = self.size // 2

    def paint(self, window):
        # Drawing the Pacman body
        pygame.draw.circle(window, YELLOW, (self.center_x, self.center_y), self.size / 2)

        # Drawing the Pacman mouth
        mouth_corner = (self.center_x, self.center_y)
        upper_lip = (self.center_x + self.radius, self.center_y - self.radius)
        lower_lip = (self.center_x + self.radius, self.center_y)
        points = [mouth_corner, upper_lip, lower_lip]

        pygame.draw.polygon(window, BLACK, points)

        # Drawing the Pacman eye
        eye_x = int(self.center_x + self.radius / 3)
        eye_y = int(self.center_y - self.radius * 0.6)

        pygame.draw.circle(window, BLACK, (eye_x, eye_y), int(self.radius / 10))
