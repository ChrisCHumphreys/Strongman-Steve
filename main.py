"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import constants
from spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
    """This class represents the player, it derives from the sprite class"""

    def __init__(self, color, width, height):
        """Constructor, pass in the color of the block,
        and its x and y position."""

        # call the parent class Sprite Constructor
        super().__init__()

        # Lists to hold our walking and jumping animations
        self.walking = False
        self.frame = 0
        self.walking_frames_r = []


        # Load in all images to create Animation
        sprite_sheet = SpriteSheet("p2_walk.png")
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
        image = sprite_sheet.get_image(0, 184, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 184, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 184, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 274, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(67, 274, 66, 90)
        self.walking_frames_r.append(image)


        # Create an image of the block and fill it with a color.
        # This could also be an image loaded from a disk


        self.image = self.walking_frames_r[0]
        # self.image.fill(color)

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
        self.velocity = -3

    def move_right(self):
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
        self.image = self.walking_frames_r[self.frame]

pygame.init()

# Set the width and height of the screen [width, height]
size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Simple Walking Animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# create an instance of Player
p1 = Player(constants.RED, 66, 90)

# Add player to a sprite grounp - as far as I can tell the only way to render
# is to have in a group first, and then to draw the group.
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(p1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # --- Movement of player controls
        elif event.type == pygame.KEYDOWN:
            # if key pressed was an arrow KEY
            if event.key == pygame.K_LEFT:
                p1.move_left()
            if event.key == pygame.K_RIGHT:
                p1.move_right()

        elif event.type == pygame.KEYUP:
            # if user let go of key - stop movement
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.stop()

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(constants.WHITE)

    # --- Drawing code should go here

    # update location of player 1 based on key presses
    p1.update()
    # draw on to screen
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
