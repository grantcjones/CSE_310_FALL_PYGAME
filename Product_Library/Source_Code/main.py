import pygame
import sys
import random
from player import Player
from tile import Tile

pygame.init()

try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing Pygame mixer: {e}")
    sys.exit(1)

# Constants
BACKGROUND = (53, 81, 92)
PLAYER_IMAGE = 'CSE_310_FALL_PYGAME/Product_Library/Source_Code/art/player.png'
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

# Player movement settings
move_speed = 4          # Speed for left/right movement
jump_height = 17        # Initial upward jump velocity
gravity = 0.5           # Gravity for a smoother fall
velocity_y = 0          # Vertical velocity
is_jumping = False       # Jumping state

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a more complex map layout
platforms = pygame.sprite.Group()
map_layout = [
    (0, 580, 1000, 20),    # Ground platform
    (150, 450, 150, 20),   # Platform 1
    (400, 380, 200, 20),   # Platform 2
    (700, 300, 180, 20),   # Platform 3
    (500, 200, 100, 20),   # Platform 4 (higher)
    (850, 150, 100, 20),   # Platform 5
    (200, 100, 150, 20),   # Platform 6
]

for x, y, width, height in map_layout:
    platforms.add(Tile(x, y, width, height))

# Load player and set starting position randomly on top of one of the platforms
player = Player(PLAYER_IMAGE)
random_platform = random.choice(map_layout)
player.rect.midbottom = (random_platform[0] + random_platform[2] // 2, random_platform[1])

# Frame rate control
clock = pygame.time.Clock()

# Game loop
while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    
    # Horizontal movement
    if keys[pygame.K_a] and player.rect.left > 0:
        player.rect.x -= move_speed
    if keys[pygame.K_d] and player.rect.right < SCREEN_WIDTH:
        player.rect.x += move_speed

    # Jump initiation
    if keys[pygame.K_SPACE]:
        if not is_jumping:  # Start jumping only if not already jumping
            is_jumping = True
            velocity_y = -jump_height

    # Apply gravity or jumping
    player.rect.y += velocity_y
    velocity_y += gravity if is_jumping else 0

    # Collision detection with platforms
    on_platform = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if velocity_y > 0:  # Player is falling
                player.rect.bottom = platform.rect.top
                velocity_y = 0
                is_jumping = False
                on_platform = True
                break

    # Apply gravity only if not on any platform
    if not on_platform and player.rect.bottom < SCREEN_HEIGHT:
        velocity_y += gravity

    # Exit condition
    if keys[pygame.K_ESCAPE]:
        break

    # Drawing
    screen.fill(BACKGROUND)
    screen.blit(player.image, player.rect)
    platforms.draw(screen)
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
