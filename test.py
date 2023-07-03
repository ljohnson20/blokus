import pygame
import numpy
import sys

import player
from block import Block
from board import Board

def main():
    main_player = player.Human((255, 0, 0), "TEST HUMAN")
    dummy_player = player.Computer((0, 72, 186), "TEST CPU")
    print(f"Human: {main_player.is_human} CPU: {dummy_player.is_human}")
    block: Block
    for block in main_player.blocks:
        for _ in range(4):
            block.rotate()
        block.flip()
        for _ in range(4):
            block.rotate(clockwise=False)

    board = Board(14)
    block = main_player.blocks[-4]
    print(block)

    # bool_array = numpy.array(block.struct, dtype=bool)
    # print(numpy.where(numpy.pad(~bool_array, ((0, 11), (0, 11)), constant_values=True), board.board, 5))

    # board.add_block(main_player.id, main_player.blocks[-4], (1,1))
    # print(board)
    # board.add_block(main_player.id, main_player.blocks[-3], (5,6))
    # print(board)
    # board.add_block(dummy_player.id, dummy_player.blocks[-8], (10,10))
    # print(board)

    # index = (1,2)
    # print(board.board[index[0],index[1]])
    # chunk, location = board.view_chunk(block, index)
    # print(chunk)
    # print(location)
    # print(f"location size: {location.shape} vs Block size: {block.shape}")
    # if location.shape[0] < block.shape[0] or location.shape[1] < block.shape[1]:
    #     print(f"Cannot place block")
    #     sys.exit(1)
    # print(numpy.where(numpy.array(block.struct, dtype=bool), location, 0).sum())
    # print(block.center_index)

if __name__ == "__main__":
    main()
