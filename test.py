import pygame, numpy
import player

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
        # Position and size
        block.rect = pygame.Rect(0, 0, width, height)
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
                            pygame.Rect(size + 1, y*size + 1,
                                size - 2, size - 2)
                        )

def main():
    main_player = player.Player((255, 0, 0), "TEST 1")
    for block in main_player.blocks:
        draw_block(block, 10)

if __name__ == "__main__":
    main()
