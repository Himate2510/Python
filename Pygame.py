import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 132, 255))
    pygame.display.flip()