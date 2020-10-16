import random, math
import pygame
from pygame.locals import *
import numpy as np
from abstract import Bubbles

# self.x = horizontal da superficie
# self.y = vertical da superficie
# self.m = Massa da esfera
# self.v = Tupla com velocidades na componente i e j
# self.width = Largura da janela
# self.height = Comprimento da janela

class Circle(Bubbles):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def check_collision(self):
        for theta in range(0, 360):
            x = int ((self.radius * math.cos(theta)) + self.x)
            y = int ((self.radius * math.sin(theta)) + self.y)
        
            color = self.surface.get_at((x, y))

            if color != self.surface_color:
                return True
        return False
    
    def check_board_collision(self):
        OFFSET = 5
        
        newx = self.x + self.v[0]
        newy = self.y + self.v[1]

        if newx <= (self.radius + OFFSET) or newx >= (self.width - self.radius - OFFSET):
            self.board_collision_x = True
            return True
        if newy <= (self.radius + OFFSET) or newy >= (self.height - self.radius - OFFSET):
            self.board_collision_y = True
            return True
        return False

    def show(self):
        pygame.draw.circle(self.surface, self.bubbles_color, (int(self.x),int(self.y)), self.radius)