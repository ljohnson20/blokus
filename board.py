import numpy
from constants import *

class Board:

    def __init__(self, board_size) -> None:
        self.board = numpy.zeros((board_size, board_size), dtype=int)

    @property
    def board_size(self):
        return self.board.shape[0]

    # Place block
    # Kill sprite from group & update

    # Find valid corners with block
