import pygame
from pygame.locals import *
import sys
from circle import Circle
from square import Square
import math, random


class BubblesGame:
    bubbles = []

    def __init__(self, SURFACE_COLOR=(0,0,0), CIRCLE_BUBBLES=1, SQUARE_BUBBLES=1, BUBBLES_COLOR=(255,255,255), BUBBLES_RADIUS=1, WIDTH=50, HEIGHT=50):
        
        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        self.surface_color = SURFACE_COLOR

        for i in range(CIRCLE_BUBBLES):
            x, y = self.build_far(BUBBLES_RADIUS, WIDTH, HEIGHT)
            self.bubbles.append(
                Circle(
                    surface=self.surface,
                    surface_color=self.surface_color,
                    bubbles_color=BUBBLES_COLOR,
                    bubbles_radius=BUBBLES_RADIUS,
                    width=WIDTH,
                    height=HEIGHT,
                    x=x,
                    y=y,
                )
            )
        for i in range(SQUARE_BUBBLES):
            x, y = self.build_far(BUBBLES_RADIUS, WIDTH, HEIGHT)
            self.bubbles.append(
                Square(
                    surface=self.surface,
                    surface_color=self.surface_color,
                    bubbles_color=BUBBLES_COLOR,
                    bubbles_radius=BUBBLES_RADIUS,
                    width=WIDTH,
                    height=HEIGHT,
                    x=x,
                    y=y,
                )
            )

    def build_far(self, radius, width, height):
        OFFSET = 3
        far = False
        distance = []

        if not self.bubbles:
            x = random.randint(radius+OFFSET, width-radius-OFFSET)
            y = random.randint(radius+OFFSET, height-radius-OFFSET)
            return x, y

        while not far:
            distance = []
            x = random.randint(radius+OFFSET, width-radius-OFFSET)
            y = random.randint(radius+OFFSET, height-radius-OFFSET)

            for bubble in self.bubbles:
                distance.append(math.sqrt(((x-bubble.x)**2) + ((y-bubble.y)**2)))

            if min(distance) > (2*radius + OFFSET):
                far = True
        
        return x, y

    def have_collision(self, bubble):
        OFFSET = 3

        newx = bubble.x + bubble.v[0]
        newy = bubble.y + bubble.v[1]

        for nearest in self.bubbles:
            if math.sqrt(((newx-nearest.x)**2)+((newy-nearest.y)**2)) <= (bubble.radius + nearest.radius + OFFSET):
                return bubble.check_collision()
        return False

    def take_the_nearest(self, bubble):
        distance = []

        for nearest in self.bubbles:
            if nearest != bubble:
                distance.append(math.sqrt(((bubble.x-nearest.x)**2)+((bubble.y-nearest.y)**2)))

        return self.bubbles[distance.index(min(distance))]
    
    def move(self):
        for bubble in self.bubbles:
            if bubble.check_board_collision():
                bubble.board_collision()
            elif self.have_collision(bubble):
                bubble.elastic_collision(self.take_the_nearest(bubble))

            bubble.move()
            bubble.show()

    def run(self):
        self.surface.fill(self.surface_color)
        self.close()
        self.move()
        pygame.display.flip()
    
    def save(self, path, name):
        file = path + str(name) + '.png'
        pygame.image.save(self.surface, file)

    def close(self):
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keystate[K_ESCAPE]:
                pygame.quit(); sys.exit()