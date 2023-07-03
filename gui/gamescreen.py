import pygame
from constants import *

from game import Game
from gui_player import GuiPlayer

# Biggest challenge is scaling for different screen sizes - via inits and pygame.display.get_surface().get_size()
# Do we redraw everything on updates or can we control what is redrawn?

# Every subclass (player, board, block) should provide a surface or sprite that can be blit in a location
# Docs - Blitting is one of the slowest operations in any game, so you need to be careful not to blit too much onto the screen in every frame

# Need to provide a winner surface to display on gameover
class GameScreen:
    def __init__(self, game: Game) -> None:
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

        self.gui_players = []
        for player in game.players:
            self.gui_players.append(GuiPlayer(player))

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
        # If it's the first update draw everything

        # If it's a player turn
        # Update game board

        # Update current player



        # Draw background and grid.
        self.screen.blit(self.background, (0, 0))
        for gui_player in self.gui_players:
            player_surface = gui_player.player_surface
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
