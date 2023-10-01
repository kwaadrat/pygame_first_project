import pygame

pygame.init()

window_size =(500, 500)

screen = pygame.display.set_mode(window_size)

background = (230, 230, 230)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            screen.fill(background)

    pygame.draw.rect(screen, (100, 150, 100), (100, 100, 100, 300, 300))

    pygame.display.flip()

pygame.quit()