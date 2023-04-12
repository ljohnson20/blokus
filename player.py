import itertools
import logging

from constants import *
from block import Block
from board import Board

class Player:
    newid = itertools.count(1).__next__

    def __init__(self, color, title) -> None:
        # Need unique incremental ID for marking squares on board
        self.id = Player.newid()

        self.color = color
        self.title = title
        self.blocks = []
        for block_struct in BLOCKS_DICT.values():
            try:
                self.blocks.append(Block(block_struct))
            except ValueError:
                logging.warning("Invalid block shape - skipping")
        self.passed = False

    # Add standard turn method
    # Should update blocks group at end to redraw missing (used) tile
    def place_block(self, board: Board, block: Block, index: tuple) -> None:
        try:
            board.add_block(self.id, block, index)
        except ValueError:
            logging.debug(f"Unable to place block at {index}")
        else:
            # If successfully placed remove the block from the players list
            self.blocks.pop(self.blocks.index(block))

    # Count total remaining tiles
    def count_points(self) -> int:
        total = 0
        for block in self.blocks:
            total += block.points
        return total

class Human(Player):

    def __init__(self, color, title) -> None:
        super().__init__(color, title)

    # def block_clicked(self, pos: tuple) -> Block:
    #     for block in self.blocks:
    #         if block.rect.collidepoint(pos):
    #             return block
    #     return None

    # Needs player screen render change for selected tile


class Computer(Player):

    def __init__(self, color, title) -> None:
        super().__init__(color, title)
