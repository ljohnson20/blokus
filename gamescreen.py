import pygame, numpy
from constants import *

class GameScreen:

    def __init__(self, game) -> None:
        self.game_data = game

        if len(game.players) > 2:
            self.tile_size = 30
        else:
            self.tile_size = 42

        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 20)

        pygame.display.set_caption("Blokus")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background = self.create_background().convert()

        self.update_screen()

    @property
    def grid_x_start(self):
        w_center = WINDOW_WIDTH // 2
        return w_center - self.game_data.board.board_size // 2 * self.tile_size
    
    @property
    def grid_y_start(self):
        h_center = WINDOW_HEIGHT // 2
        return h_center - self.game_data.board.board_size // 2 * self.tile_size

    def update_screen(self):
        # Draw background and grid.
        self.screen.blit(self.background, (0, 0))
        for player_surface in self.player_surfaces:
            player_surface.update()
            self.screen.blit(player_surface.surface, player_surface.corner_cords)
        # Update
        pygame.display.flip()

    def create_background(self) -> pygame.Surface:
        # Create background.
        background = pygame.Surface(self.screen.get_size())
        background.fill(BG_COLOR)
        
        self.create_grid(background)
        self.create_player_spaces(background)

        return background

    def create_grid(self, background: pygame.Surface):
        # Draw the grid on top of the background.
        for x in range(self.game_data.board.board_size):
            for y in range(self.game_data.board.board_size):
                rect = pygame.Rect(
                    self.grid_x_start + x * self.tile_size, 
                    self.grid_y_start + y * self.tile_size, 
                    self.tile_size, self.tile_size
                )
                pygame.draw.rect(background, GRID_COLOR, rect, 1)
        border_rect = pygame.Rect(
            self.grid_x_start, self.grid_y_start,
            self.game_data.board.board_size * self.tile_size, 
            self.game_data.board.board_size * self.tile_size
        )
        pygame.draw.rect(background, GRID_COLOR, border_rect, 3)

    def create_player_spaces(self, background: pygame.Surface):
        player_width = self.grid_x_start - 20
        player_hight = WINDOW_HEIGHT // 2 - 20
        # Draw player squares
        self.player_surfaces = []
        for i, player in enumerate(self.game_data.players):
            flip_sides = i % 2 * (self.grid_x_start + self.game_data.board.board_size * self.tile_size)
            player_start = 10
            if i >= 2:
                player_start = WINDOW_HEIGHT // 2 + 10
            player_title = pygame.Rect(flip_sides + 10, player_start, player_width, 30)
            player_rect = pygame.Rect(flip_sides + 10, player_start, player_width, player_hight)
            pygame.draw.rect(background, player.color, player_rect, 2, 8)
            pygame.draw.rect(background, player.color, player_title, 2, -1, 8, 8, 1, 1)
            player_name = self.small_font.render(player.title, True, player.color)
            background.blit(player_name, player_title.center)

            self.player_surfaces.append(PlayerSurface(player, (player_width - 10, player_hight - 40), 
                                                    (flip_sides + 15, player_start + 30)))
    
    @staticmethod
    def draw_block(block: pygame.sprite.DirtySprite, size: int):
        if type(block.struct[0]) == numpy.ndarray:
            width = len(block.struct[0]) * size
        else:
            width = size
        if type(block.struct) == numpy.ndarray:
            height = len(block.struct) * size
        else:
            height = size
        block.image = pygame.surface.Surface([width, height])
        block.image.set_colorkey((0, 0, 0))
        for y, row in enumerate(block.struct):
            if type(row) == numpy.ndarray:
                for x, col in enumerate(row):
                    if col:
                        pygame.draw.rect(
                            block.image,
                            block.color,
                            pygame.Rect(x*size + 1, y*size + 1,
                                size - 2, size - 2)
                        )
            else:
                pygame.draw.rect( block.image, block.color,
                            pygame.Rect(1, y*size + 1,
                                size - 2, size - 2)
                        )

class PlayerSurface:

    def __init__(self, player, dimensions: tuple, corner_cords: tuple) -> None:
        self.surface = pygame.Surface(dimensions)
        self.surface.fill(BG_COLOR)
        self.corner_cords = corner_cords
        self.player = player
            
    def update(self):
        draw_x, draw_y = 5, 5
        max_y = 0
        for block in self.player.blocks:
            GameScreen.draw_block(block, 15)
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
            
            

