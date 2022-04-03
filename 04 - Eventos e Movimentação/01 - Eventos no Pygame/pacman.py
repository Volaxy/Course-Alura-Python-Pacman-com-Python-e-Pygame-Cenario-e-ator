import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Pacman:
    def __init__(self):
        self.center_x = 400
        self.center_y = 300
        self.size = 800 // 30
        self.radius = self.size // 2

        self.speed_x = 1
        self.speed_y = 1

        self.line = 1
        self.column = 1

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

    def calculate_rules(self):
        self.line += self.speed_x
        self.column += self.speed_y

        self.center_x = int(self.line * self.size + self.radius)
        self.center_y = int(self.column * self.size + self.radius)

        if self.center_x + self.radius > 800:
            self.speed_x = -1
        if self.center_x - self.radius < 0:
            self.speed_x = 1

        if self.center_y + self.radius > 600:
            self.speed_y = -1
        if self.center_y - self.radius < 0:
            self.speed_y = 1
