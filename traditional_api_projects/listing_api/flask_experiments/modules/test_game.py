import pygame

pygame.init()

# Set screen size
screen = pygame.display.set_mode((400, 300))

# Set character starting position
x = 200
y = 150

# Set game loop
done = False
while not done:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get pressed keys
    pressed = pygame.key.get_pressed()

    # Move character left or right
    if pressed[pygame.K_LEFT]:
        x -= .5
    if pressed[pygame.K_RIGHT]:
        x += .5

    # Draw character
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 60, 60))

    # Update screen
    pygame.display.flip()