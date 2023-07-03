import pygame
import numpy

from block import Block

# How do we redraw the bock on rotations/flips
# How can we center the mouse on the 2 center index
class GuiBlock(pygame.sprite.Sprite):
    def __init__(self, block: Block, color: tuple, *groups: pygame.sprite._Group) -> None:
        self.selected = False
        self.color = color
        # Provide pygame.Surface for the block image
        self.image = self.draw_block(block, color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        super().__init__(*groups)

    # If the block has been selected have it follow the mouse
    def update(self):
        pos = pygame.mouse.get_pos()

    @staticmethod
    def draw_block(block: Block, color: tuple, size: int) -> pygame.surface.SurfaceType:
        if type(block.struct[0]) == numpy.ndarray:
            width = len(block.struct[0]) * size
        else:
            width = size
        if type(block.struct) == numpy.ndarray:
            height = len(block.struct) * size
        else:
            height = size
        image = pygame.surface.Surface([width, height])
        image.set_colorkey((0, 0, 0))
        for y, row in enumerate(block.struct):
            if type(row) == numpy.ndarray:
                for x, col in enumerate(row):
                    if col:
                        pygame.draw.rect(
                            image,
                            color,
                            pygame.Rect(x*size + 1, y*size + 1,
                                size - 2, size - 2)
                        )
            else:
                pygame.draw.rect( image, color,
                            pygame.Rect(1, y*size + 1,
                                size - 2, size - 2)
                        )
        return image
