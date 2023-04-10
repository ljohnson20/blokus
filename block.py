import pygame, numpy

class Block(pygame.sprite.Sprite):

    def __init__(self, shape, color):
        super().__init__()
        self.color = color
        self.struct = numpy.array(shape, dtype=int)
    
    def update(self):
        pass

    # Update for larger screen

    # Count squares in shape

    # Rotate 90 degrees - clockwise & counterclockwise

    # Flip block

    # Corners?

