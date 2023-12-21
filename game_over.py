import pygame


def draw_game_over(screen, quit_button):
    screen.fill((255, 255, 255))

    image = pygame.image.load("images/game/sky/sky1.png").convert()

    image = pygame.transform.scale(image, (800, 600))

    screen.blit(image, (0, 0))

    font = pygame.font.Font(None, 36)
    end_str = "Game Over :)"
    text = font.render(end_str, True, (0, 0, 0))
    screen.blit(text, (300, 200))

    footer_image = pygame.image.load("images/game/plane/plane-fov.png").convert_alpha()
    footer_image = pygame.transform.scale(footer_image, (800, 600))
    screen.blit(footer_image, (0, 0))

    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button, 2)
    text = font.render("Quit", True, (0, 0, 0))
    screen.blit(text, (700, 550))
