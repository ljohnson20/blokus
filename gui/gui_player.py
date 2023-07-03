import pygame

from constants import *
from player import Player
from gui_block import GuiBlock

# Is there a way to update the player blocks when the base player blocks are modified
class GuiPlayer:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.gui_blocks = pygame.sprite.Group()
        for block in player.blocks:
            GuiBlock(block, player.color, )
        self.player_surface = PlayerSurface(self)

    def update(self):
        pass

class PlayerSurface:
    def __init__(self, player: GuiPlayer, dimensions: tuple, corner_cords: tuple) -> None:
        self.surface = pygame.Surface(dimensions)
        self.surface.fill(BG_COLOR)
        self.corner_cords = corner_cords
        self.game_player = player
            
    def update(self):
        draw_x, draw_y = 5, 5
        max_y = 0
        for block in self.game_player.blocks:
            move_x, move_y = block.image.get_size()
            if move_y > max_y:
                max_y = move_y
            if draw_x + move_x > self.surface.get_size()[0]:
                draw_x = 5
                draw_y += max_y + 8
                max_y = 0
            self.surface.blit(block.image, (draw_x, draw_y))
            # Update block rectangle
            block.rect = block.image.get_rect()
            draw_x += move_x + 5
