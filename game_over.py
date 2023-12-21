import pygame


def draw_game_over(screen, quit_button):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, (0, 0, 0))
    screen.blit(text, (300, 200))
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button, 2)
    text = font.render("Quit", True, (0, 0, 0))
    screen.blit(text, (350, 350))
