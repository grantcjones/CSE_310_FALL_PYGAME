import pygame
import sys
import random

from player import Player

pygame.init()

try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing Pygame mixer: {e}")
    sys.exit(1)

BACKGROUND = (53, 81, 92)
PLAYER = 'Product_Library/Source_Code/art/player.png'

is_jumping = False
jump_height = 15  # Jump strength (adjust as needed)
gravity = 1       # Gravity strength
velocity_y = 0    # Vertical speed

screen = pygame.display.set_mode((1000, 1000))

player = Player(PLAYER)

while True:
    pygame.event.pump()  # Keeps the window responsive
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.rect.left > 0:
        player.rect.x -= 1

    if keys[pygame.K_d] and player.rect.right < 1000:
        player.rect.x += 1

    if keys[pygame.K_s] and player.rect.bottom < 980:
        player.rect.y += 1

    # Gravity
    if player.rect.bottom < 960:
        player.rect.y += 1


    if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            velocity_y = -jump_height  # Initiate jump by setting upward velocity

    # Apply gravity
    if is_jumping:
        player.rect.y += velocity_y
        velocity_y += gravity  # Gravity increases downward speed

        # Check if player has landed (e.g., at the bottom of the screen)
        if player.rect.bottom >= 960:  # Adjust for the ground level
            player.rect.bottom = 960
            is_jumping = False
            velocity_y = 0  # Reset vertical speed on landing

    # Apply gravity when not jumping
    elif player.rect.bottom < 960:
        player.rect.y += gravity
    
    if keys[pygame.K_ESCAPE]:
        break

    screen.fill(BACKGROUND)
    screen.blit(player.image, player.rect)  # Draw player on the screen
    pygame.display.flip()  # Update the display

pygame.quit()
