import random, math
import pygame
from pygame.locals import *
import numpy as np
from abstract import Bubbles

class Square(Bubbles):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
    def check_collision(self):
        for x in range(int(self.x - (self.z/2)), int(self.x + (self.z/2))):
            y_upper = self.y - self.w/2
            y_lower = self.y + self.w/2

            color_side_upper = self.surface.get_at((int(x), int(y_upper)))
            color_side_lower = self.surface.get_at((int(x), int(y_lower)))

            if (color_side_upper != self.surface_color) or (color_side_lower != self.surface_color):
                return True

        for y in range(int(self.y - (self.w/2)), int(self.y + (self.w/2))):
            x_left = self.x - self.z/2
            x_right = self.x + self.z/2

            color_side_left = self.surface.get_at((int(x_left), int(y)))
            color_side_right = self.surface.get_at((int(x_right), int(y)))

            if (color_side_left != self.surface_color) or (color_side_right != self.surface_color):
                return True
    
        return False
    
    def check_board_collision(self):
        OFFSET = 5
        
        newx = self.x + self.v[0] - (self.z/2)
        newy = self.y + self.v[1] - (self.w/2)

        if newx <= OFFSET or newx >= (self.width - self.w - OFFSET):
            self.board_collision_x = True
            return True
        if newy <= OFFSET or newy >= (self.height - self.w - OFFSET):
            self.board_collision_y = True
            return True
        return False

    def show(self):
        # Assume-se que x e y sao coordenadas do centro do quadrado. Porem, para desenhar o quadrado, 
        # as coordenadas que precisamos sao as coordenadas do vertice superior esquerdo, por isso
        # eh necessario ajustar as coordenadas sempre que for preciso

        x = self.x - self.z/2
        y = self.y - self.w/2
        pygame.draw.rect(self.surface, self.bubbles_color,(int(x),int(y),int(self.z),int(self.w)))