import pygame

class Sprite:
    def __init__(self, image, center):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center
    
    def render(self):
        surface.blit(self.image, self.rect)




WINDOW_SIZE = [800,600]
MAX_FPS = 60

window = pygame.Window('Tower Defense', WINDOW_SIZE)
surface = window.get_surface()
clock = pygame.Clock()

image = pygame.Surface([50,50])
image.fill("red")
player = Sprite(image, [WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2])



running = True
while running:
    #Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False

    #Обновление объектов


    #Отрисовка
    surface.fill('black')
    player.render()
    window.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())
