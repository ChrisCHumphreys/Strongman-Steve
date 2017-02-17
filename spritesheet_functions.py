"""
This module is used to pull individual sprites from sprite sheets
"""

import pygame
import constants

class SpriteSheet(object):
    """ Class used to pull image from spritesheet """

    def __init__(self, file_name):
        """constructor, pass in the file name of the spritesheet"""

        # Load the spritesheet
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger sprite sheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite """

        # create a new blank image
        image = pygame.Surface([width, height]).convert()

        # copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # return the image
        return image
