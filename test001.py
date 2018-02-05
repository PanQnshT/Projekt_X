import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
player = pygame.Rect(0,0,25,25)
clock = pygame.time.Clock()

while True:

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    # Input

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 1
    if keys[pygame.K_DOWN]:
        player.y += 1
    if keys[pygame.K_RIGHT]:
        player.x += 1
    if keys[pygame.K_LEFT]:
        player.x -= 1

    # Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(50,100,200),player)
    pygame.display.flip()
