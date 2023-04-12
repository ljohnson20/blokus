import numpy

from typing import Tuple

class Block:
    def __init__(self, struct):
        self.struct = numpy.array(struct, dtype=int)
        self._validate_block()
    
    def __repr__(self):
        return f"{self.struct}"

    def update(self):
        pass

    def _validate_block(self) -> bool:
        # Check for single 2 in struct
        if numpy.count_nonzero(self.struct > 1) != 1:
            raise ValueError("Need single 2 in block struct")
        
        # TODO - Check for no gaps in struct

    # Rotate 90 degrees - clockwise & counterclockwise
    # TODO - Is there a way to return itself to allow for block.rotate().rotate() or block = block_list[-1].rotate()
    def rotate(self, clockwise: bool = True) -> None:
        # If the struct is 1d need to do a resize to "rotate" instead
        if self.struct.ndim == 1:
            self.struct = numpy.reshape(self.struct, (self.struct.size, 1))
        
        if clockwise:
            self.struct = numpy.rot90(self.struct, k=-1)
        else:
            self.struct = numpy.rot90(self.struct)

    # Flip block
    def flip(self) -> None:
        # Check if array is 2d and flip left/right if so
        if self.struct.ndim > 1:
            self.struct = numpy.fliplr(self.struct)
    
    def block_margins(self, index: tuple) -> Tuple[int, int, int, int]:
        # Need to manipulate 1d block.structs to something we can add with
        if self.struct.ndim == 1:
            size = (1,self.struct.size)
        else:
            size = self.struct.shape
        # Calculate proper bounds on game board
        upper_bound = index[0] - self.center_index[0]
        lower_bound = upper_bound + size[0]
        left_bound = index[1] - self.center_index[1]
        right_bound = left_bound + size[1]

        return (upper_bound, lower_bound, left_bound, right_bound)

    # Count filled in blocks in struct
    @property
    def points(self) -> int:
        return numpy.count_nonzero(self.struct)

    # Use numpy shape a lot so make it easier to return
    @property
    def shape(self) -> numpy.ndarray.shape:
        return self.struct.shape
    
    # Need to get the "center" (2) index
    @property
    def center_index(self) -> Tuple[int, int]:
        i, j = numpy.where(self.struct == 2)
        return (i[0], j[0])

    # Corners?

