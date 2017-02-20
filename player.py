import pygame
from spritesheet_functions import SpriteSheet
import constants

class Player(pygame.sprite.Sprite):
    """This class represents the player, it derives from the sprite class"""

    def __init__(self, sprite_sheet_walking):
        """Constructor, pass in the sprite sheet of the walking animation"""

        # call the parent class Sprite Constructor
        super().__init__()

        # Lists to hold our walking and jumping animations
        self.walking = False
        self.frame = 0
        self.walking_frames_r = []
        self.walking_frames_l = []
        self.walking_direction = "r"

        # Load in all images to create Animation
        # - Walking Right
        sprite_sheet = SpriteSheet(sprite_sheet_walking)
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 186, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 186, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 280, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(67, 280, 66, 90)
        self.walking_frames_r.append(image)

        # - Walking Left
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 186, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 186, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 280, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(67, 280, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]

        # Fetch the rectangular object that has the dimensions of the image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # starting location
        self.rect.x = 0
        self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

        # set inital velocity to O - or not moving
        self.velocity = 0

    def move_left(self):
        self.walking_direction = "l"
        self.velocity = -3
        self.frame += 1
        self.walking = True


    def move_right(self):
        self.walking_direction = "r"
        self.velocity = 3
        self.frame += 1
        self.walking = True
        # self.image = self.walking_frames_r[self.frame]

    def stop(self):
        self.velocity = 0
        self.walking = False
        self.frame = 0
        # self.image = self.walking_frames_r[self.frame]

    def update(self):
        self.rect.x += self.velocity
        if self.walking:
            self.frame += 1
            if self.frame > 10:
                self.frame = 0
        if self.walking_direction == "r":
            self.image = self.walking_frames_r[self.frame]
        if self.walking_direction == "l":
            self.image = self.walking_frames_l[self.frame]
