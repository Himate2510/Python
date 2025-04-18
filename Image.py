import pygame
pygame.init()
s = pygame.display.set_mode((800,1080))
c = pygame.image.load("Ayrton.jpeg.jpg").convert_alpha()
c = pygame.transform.scale(c, (400,400))
while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    s.fill((219, 115, 29))
    s.blit(c,(200,200))
    pygame.display.flip()