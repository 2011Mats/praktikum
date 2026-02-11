import pygame

pygame.init()

BASE_WIDTH = 800
BASE_HEIGHT = 600

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw game to base surface
    game_surface.fill((0, 0, 0))

    # Scale to screen
    scaled_surface = pygame.transform.scale(
        game_surface, (screen_width, screen_height)
    )

    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()