import pygame
import sys
from menu import draw_menu
from game import update_game, draw_game, Airplane
from game_over import draw_game_over
from config import WIDTH, HEIGHT, FPS, MENU, PLAYING, GAME_OVER, current_state

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Battle")

clock = pygame.time.Clock()
running = True
play_button = pygame.Rect(300, 200, 200, 100)
quit_button = pygame.Rect(650, 530, 200, 100)
airplane = Airplane()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == MENU and play_button.collidepoint(event.pos):
                current_state = PLAYING
            elif current_state == PLAYING:
                if quit_button.collidepoint(event.pos):
                    current_state = GAME_OVER
            elif current_state == GAME_OVER and quit_button.collidepoint(event.pos):
                running = False

    keys = pygame.key.get_pressed()
    airplane.update(keys)

    if current_state == MENU:
        draw_menu(screen, play_button)
    elif current_state == PLAYING:
        update_game()
        draw_game(screen, quit_button, airplane)
    elif current_state == GAME_OVER:
        draw_game_over(screen, quit_button)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
