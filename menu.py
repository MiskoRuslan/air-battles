import pygame
import os


def draw_menu(screen, play_button):
    background_images = [
        pygame.image.load(os.path.join("images/menu/menu_background_1.jpg")),
        pygame.image.load(os.path.join("images/menu/menu_background_2.jpg")),
        pygame.image.load(os.path.join("images/menu/menu_background_3.jpg")),
    ]

    for i in range(1, 3):
        screen.blit(background_images[i], (0, 0))

    font_path = os.path.join("fonts/pixel_font.ttf")
    font = pygame.font.Font(font_path, 36)
    pygame.draw.rect(screen, (0, 200, 0), play_button)
    pygame.draw.rect(screen, (0, 0, 0), play_button, 2)
    text = font.render("Start", True, (0, 0, 0))
    screen.blit(text, (355, 235))
