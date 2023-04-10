import pygame
from constants import *
from block import Block

class Player:

    def __init__(self, color, title) -> None:
        self.color = color
        self.title = title
        self.blocks = pygame.sprite.Group()
        for block in BLOCKS_DICT.values():
            self.add(Block(block, color))
        self.passed = False
    
    # Add standard turn method
    # Should update blocks group at end to redraw missing (used) tile

    # Count tiles method

class Human(Player):

    def __init__(self, color, title) -> None:
        super().__init__(color, title)

    def block_clicked(self, pos: tuple) -> Block:
        for block in self.blocks:
            if block.rect.collidepoint(pos):
                return block
        return None

    # Needs player screen render change for selected tile


class Computer(Player):

    def __init__(self, color, title) -> None:
        super().__init__(color, title)
