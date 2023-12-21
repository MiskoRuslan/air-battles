import pygame
import sys
from menu import draw_menu
from game import update_game, draw_game
from game_over import draw_game_over

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Battle")

MENU = 0
PLAYING = 1
GAME_OVER = 2
current_state = MENU

clock = pygame.time.Clock()
running = True

play_button = pygame.Rect(300, 200, 200, 100)
quit_button = pygame.Rect(300, 300, 200, 100)

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

    if current_state == MENU:
        draw_menu(screen, play_button)
    elif current_state == PLAYING:
        update_game()
        draw_game(screen, quit_button)
    elif current_state == GAME_OVER:
        draw_game_over(screen, quit_button)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
