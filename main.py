import pygame


WINDOW_SIZE = [800,600]
MAX_FPS = 60

window = pygame.window('Tower Defense', WINDOW_SIZE)
surface = window.get_surface()
clock = pygame.Clock()
running = True
while running:
    #Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False

    #Обновление объектов


    #Отрисовка
    surface.fill('black')
    
    window.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())
