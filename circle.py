import pygame
pygame.init()

window = pygame.display.set_mode((600, 600))

window.fill((255, 255, 1))

GREEN = (0, 255, 0)

pygame.draw.circle(window, GREEN, (100, 100), 50)

pygame.draw.circle(window, GREEN, (200, 100), 50, 5)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()