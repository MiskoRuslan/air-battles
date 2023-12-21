import pygame
import os


def draw_menu(screen, play_button):
    background_image_1 = pygame.image.load(os.path.join("images/menu/menu_background_1.jpg"))
    background_image_1 = pygame.transform.scale(background_image_1, (800, 600))

    background_image_2 = pygame.image.load(os.path.join("images/menu/menu_background_3.jpg"))
    background_image_2 = pygame.transform.scale(background_image_2, (800, 600))

    background_image_3 = pygame.image.load(os.path.join("images/menu/menu_background_3.jpg"))
    background_image_3 = pygame.transform.scale(background_image_3, (800, 600))
    screen.blit(background_image_1, (0, 0))

    font_path = os.path.join("fonts/pixel_font.ttf")
    font = pygame.font.Font(font_path, 36)
    pygame.draw.rect(screen, (0, 200, 0), play_button)
    pygame.draw.rect(screen, (0, 0, 0), play_button, 2)
    text = font.render("Start", True, (0, 0, 0))
    screen.blit(text, (355, 235))
