# platform class that will create all surfaces in the game

import pygame
from spritesheet_functions import SpriteSheet

""" These constants define out platform types """
# Name of file
# X Location of Sprite
# Y Location of Sprite
# Width of Sprite
# Height of Sprite

GRASS_LEFT              = (503, 648, 72, 72)
GRASS_MIDDLE            = (503, 575, 72, 72)
GRASS_RIGHT             = (503, 503, 72, 72)
STONE_PLATFORM_LEFT     = (143, 863, 72, 72)
STONE_PLATFORM_RIGHT    = (143, 719, 72, 72)
STONE_PLATFORM_MIDDLE   = (143, 791, 72, 72)


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on"""

    def __init__(self, sprite_sheet_data):
        """ Platform Constructor.  Assumes constructed with user passing in
            an array of 5 numbers like whats defined at the top of this
            code. """

        super().__init__()

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the Platform.
            If the player is in the way, it will shove the player
            out of the way.  This does NOT handle what happens if a
            platform shoves a player into another object.  Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/Right
        self.rect.x += self.change_x

        # see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player.  Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit.
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            # Otherwise if we are moving left, do opposite
            else:
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to change direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
