import numpy
from typing import Tuple
import logging

from block import Block

class Board:
    def __init__(self, board_size) -> None:
        # self.board = numpy.arange(board_size*board_size).reshape(board_size, board_size)
        self.board = numpy.zeros((board_size, board_size), dtype=int)

    def __repr__(self):
        return f"{self.board}"

    @property
    def board_size(self):
        return self.board.shape[0]

    # Index will be the location on the board which will always align
    # with the 2 index on the block struct
    def add_block(self, player_id: int, block: Block, index: tuple) -> None:
        # Not sure if these placement checks should be with the player, block, or here
        chunk, location = self.view_chunk(block, index)
        bool_array = numpy.array(block.struct, dtype=bool)
        # Check if there is enough space to place block at designated index
        if location.shape[0] < block.shape[0] or location.shape[1] < block.shape[1]:
            raise ValueError("Cannot place block at index - Not enough room")
        
        # Check that block does not overlap with others
        if numpy.where(bool_array, location, 0).sum():
            raise ValueError("Cannot place block at index - Overlaps with other block")

        # Check that block only touches it's own pieces corners
        # or if it's the first piece the game board corners

        bounds = block.block_margins(index)
        # Add block denoted by player id
        self.board = numpy.where(
            numpy.pad(
                ~bool_array,
                ((bounds[0], self.board_size - bounds[1]), (bounds[2], self.board_size - bounds[3])),
                constant_values=True
            ),
            self.board, player_id
        )

    # This gives back the chunk surrounding the shape placement (for checking corners/edges)
    # along with the exact shape placement (for checking size and overlaps)
    # TODO - Is there a better way to calculate this? Perhaps we just view the whole board?
    def view_chunk(self, block: Block, index: tuple) -> Tuple[numpy.ndarray, numpy.ndarray]:
        bounds = block.block_margins(index)

        logging.debug(f"[{bounds[0]}:{bounds[1]}, {bounds[2]}:{bounds[3]}]")

        # Generating chunk +1 margins if possible
        margin_x = 0
        margin_y = 0
        if bounds[0] > 0:
            margin_x = 1
        if bounds[2] > 0:
            margin_y = 1
        
        # Surprisingly if you go over the board size it just cuts it off
        # Might come back to bite us when placing in far edges
        return self.board[bounds[0]-margin_x:bounds[1]+1, bounds[2]-margin_y:bounds[3]+1], self.board[bounds[0]:bounds[1], bounds[2]:bounds[3]]

    # Place block
    # Kill sprite from group & update
