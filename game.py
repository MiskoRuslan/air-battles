import pygame
import os
import time
from config import WIDTH, HEIGHT


SHOOT_INTERVAL = 0.1
SHOOT_COUNT = 5


TOTAL_SHOOTS = 0
TOTAL_RECHARGE_TIME = 0

LAST_SHOOT_TIME = time.time()


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


class Airplane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load(os.path.join("images/game/plane/plane.png")).convert_alpha()
        self.image = pygame.transform.scale(original_image, (400, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 10
        self.bullets = pygame.sprite.Group()
        self.shoot_sound = pygame.mixer.Sound("sounds/shot-auto.wav")
        self.bombs = pygame.sprite.Group()
        self.bomb_sound = pygame.mixer.Sound("sounds/bomb-sound.wav")

    def update(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_s]:
            self.drop_bomb()

    def shoot(self):
        bullet1 = Bullet(self.rect.centerx - 50, self.rect.top)
        bullet2 = Bullet(self.rect.centerx + 50, self.rect.top)
        self.bullets.add(bullet1, bullet2)
        self.shoot_sound.play()

    def drop_bomb(self):
        bomb = Bomb(self.rect.centerx, self.rect.bottom)
        self.bombs.add(bomb)
        self.bomb_sound.play()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.midbottom = (x, y + 140)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load("images/game/bomb.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y - 100)
        self.speed = 10

    def update(self):
        self.rect.y += self.speed


def draw_game(screen, quit_button, airplane):
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
    screen.blit(text, (700, 550))
    screen.blit(airplane.image, airplane.rect)
    for bullet in airplane.bullets:
        screen.blit(bullet.image, bullet.rect)

    airplane.bullets.update()
    airplane.bullets.draw(screen)

    for bomb in airplane.bombs:
        screen.blit(bomb.image, bomb.rect)

    airplane.bombs.update()
    airplane.bombs.draw(screen)

    global LAST_SHOOT_TIME, TOTAL_SHOOTS, TOTAL_RECHARGE_TIME
    current_time = time.time()
    if current_time - LAST_SHOOT_TIME >= SHOOT_INTERVAL:
        for _ in range(SHOOT_COUNT):
            airplane.shoot()
            TOTAL_SHOOTS += 1
        LAST_SHOOT_TIME = current_time
        TOTAL_RECHARGE_TIME += SHOOT_INTERVAL

    with open("shoots_stats.txt", "w") as file:
        file.write(f"Shoots: {TOTAL_SHOOTS}, Recharge Time: {TOTAL_RECHARGE_TIME}")
