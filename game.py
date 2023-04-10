import pygame, sys
from pygame.locals import *
from constants import *
from board import Board
from player import Human, Computer
from gamescreen import GameScreen

class Game:

    def __init__(self, players: int, display: bool = True) -> None:
        self.gameover = False
        
        if players == 2:
            self.board = Board(14)
        elif players > 2 and players < 5:
            self.board = Board(20)
        else:
            print("Invalid player count need to select between 2-4")
            raise ValueError

        self.players = []
        for i in range(players):
            self.players.append(Human(PLAYER_COLORS[i], f"CPU {i+1}"))

        if display:
            self.screen = GameScreen(self)

    @property
    def player_count(self):
        return len(self.players)

    def run(self):
        running = True
        # The main game loop
        while running:
            if self.gameover == True:
                # Calculate blocks remaining per player and lowest wins
                break
            # Get inputs
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(f"Clicked at {pos}")
                    block = self.players[0].block_clicked(pos)
                    if block:
                        print(f"Clicked on block...\n{block.struct}")

                # Processing
                # This section will be built out later

            if self.screen:
                self.screen.update_screen()

def main():
    pygame.init()
    main_game = Game(4)
    main_game.run()
    pygame.quit()
    
if __name__ == "__main__":
    main()
