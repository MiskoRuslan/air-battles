import pygame
import sys

from config import WIDTH, HEIGHT, FPS, BLACK, WHITE

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air battles")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
