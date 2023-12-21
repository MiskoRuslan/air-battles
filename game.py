import pygame
import os
import time


def update_game():
    pass


def load_background_images():
    image1 = pygame.image.load(os.path.join("images/game/sky/sky1.png")).convert()
    image2 = pygame.image.load(os.path.join("images/game/sky/sky2.png")).convert()
    image3 = pygame.image.load(os.path.join("images/game/sky/sky3.png")).convert()
    image4 = pygame.image.load(os.path.join("images/game/sky/sky4.png")).convert()
    image5 = pygame.image.load(os.path.join("images/game/sky/sky5.png")).convert()
    background_images = [image1, image2, image3, image4, image5]
    for i in range(1, 5):
        image_path = os.path.join(f"images/game/sky/sky{i}.png")
        background_images.append(pygame.image.load(image_path).convert())
    return background_images


def draw_game(screen, quit_button):
    background_images = load_background_images()
    screen.fill((255, 255, 255))

    current_time = time.time()
    frame_duration = 0.5
    current_frame = int((current_time % (len(background_images) * frame_duration)) // frame_duration)
    screen.blit(background_images[current_frame], (0, 0))

    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button, 2)
    font = pygame.font.Font(None, 36)
    text = font.render("Quit", True, (0, 0, 0))
    screen.blit(text, (400, 500))

