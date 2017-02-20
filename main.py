""" My version of a platformer, done with a ton of
    guidance from http://www.balloonbuilding.com/ and
    the Programming Arcade Games with Python and pygame
    tutorials. """

import pygame
import player
import constants

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
p1 = player.Player(constants.PLAYER_WALKING_SPRITESHEET)

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
