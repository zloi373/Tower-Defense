import pygame
from random import randint



class Sprite:
    def __init__(self, image, center):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self):
        surface.blit(self.image, self.rect)


class MovingSprite(Sprite):
    def __init__(self, image, center, speed, direction):
        super().__init__(image, center)

        self.speed = speed
        self.direction = direction.normalize()

    def update(self):
        vector = self.speed * self.direction
        self.rect.move_ip(vector)


WINDOW_SIZE = [800, 600]
MAX_FPS = 60

pygame.init()

window = pygame.Window("Tower Defense", WINDOW_SIZE)
surface = window.get_surface()
clock = pygame.Clock()
font = pygame.Font(None, 64)

image = pygame.Surface([50, 50])
image.fill("green")
player = Sprite(image, [WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2])

bullets = []
enemies = []
score = 0

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            image = pygame.Surface([6, 6])
            image.fill("blue")
            bullet = MovingSprite(image, center, 7.5, pos - center)
            bullets.append(bullet)

    # Обновление объектов
    if randint(0,100) <= 3:
        image = pygame.Surface((50,50))
        image.fill('red')
        speed = randint(200,500) / 100
        center = pygame.Vector2(player.rect.center)

        r = randint(1, 4)
        if r == 1:
            pos = pygame.Vector2(
                randint(0, WINDOW_SIZE[0]),
                -100,
            )
        elif r == 2:
            pos = pygame.Vector2(
                WINDOW_SIZE[0] + 100,
                randint(0, WINDOW_SIZE[1]), 
            )
        elif r == 3:
            pos = pygame.Vector2(
                randint(0, WINDOW_SIZE[0]),
                WINDOW_SIZE[1] + 100,
            )
        else:
            pos = pygame.Vector2(
                -100,
                randint(0, WINDOW_SIZE[1]),
            )
        enemy = MovingSprite(image, pos, speed, center - pos)
        enemies.append(enemy)


    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score = 0
            enemies.clear()
            bullets.clear()
            break
    
    

    

    # Отрисовка
    surface.fill("white")
    player.render()
    for bullet in bullets:
        bullet.render()
    for enemy in enemies:
        enemy.render()
    
    text = 'Счёт:' + str(score)
    image.font.render(text,True, 'black')
    surface.blit(image, (10,10))
    window.flip()

    clock.tick(MAX_FPS)
