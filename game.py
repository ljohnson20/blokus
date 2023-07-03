import itertools
import sys
import logging

import pygame

from constants import *
from board import Board
from player import Player, Human, Computer
from gui.gamescreen import GameScreen

class Game:
    def __init__(self, players: int, gui: bool = True) -> None:
        self.gameover = False
        
        if players == 2:
            self.board = Board(14)
        elif players > 2 and players < 5:
            self.board = Board(20)
        else:
            raise ValueError("Invalid player count need to select between 2-4")

        self.players = []
        for i in range(players):
            self.players.append(Human(PLAYER_COLORS[i], f"Player {i+1}"))
        self._player_loop = itertools.cycle(self.players)
        self.current_player: Player = next(self._player_loop)

        if gui:
            self.screen = GameScreen(self)

    @property
    def player_count(self):
        return len(self.players)
    
    @property
    def gui(self) -> bool:
        return hasattr(self, "screen")

    def run(self):
        running = True
        # The main game loop
        while running:
            if self.gameover == True:
                # Calculate blocks remaining per player and lowest wins
                final_totals = [player.count_points() for player in self.players]
                # TODO - Account for a tie? Tiebreaker?
                winner = self.players[final_totals.index(min(final_totals))]
                break
            if not self.current_player.passed:
                self.current_player = next(self.player_loop)
                continue
            # Get inputs if human
            if self.current_player.is_human:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and self.gui:
                        pos = pygame.mouse.get_pos()
                        logging.debug(f"Clicked at {pos}")
                        block = self.current_player.block_clicked(pos)
                        if block:
                            logging.debug(f"Clicked on block...\n{block.struct}")

                    # Processing
                    # This section will be built out later

            # Auto perform move if CPU
            else:
                logging.info("CPU taking its turn")
            
            self.current_player = next(self._player_loop)

            # If all players have passed flip gameover flag
            if all([player.passed for player in self.players]):
                self.gameover = True

            if self.gui:
                self.screen.update_screen()

def main():
    pygame.init()
    main_game = Game(4)
    main_game.run()
    pygame.quit()
    
if __name__ == "__main__":
    main()
