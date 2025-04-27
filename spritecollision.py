import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Sprite Collision")
orange = (255,165,0)
white = (255,255,255)
navyblue = (0,0,128)
p = pygame.Rect(50,50,50,50)
o = pygame.Rect(300,200,60,60)
run = True
pv = True
speed = 5
ov = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    is1 = pygame.key.get_pressed()
    if is1[pygame.K_LEFT]:
        p.x -= speed
    if is1[pygame.K_RIGHT]:
        p.x += speed
    if is1[pygame.K_UP]:
        p.y -= speed
    if is1[pygame.K_DOWN]:
        p.y += speed
    if p.colliderect(o):
        ov = False
    screen.fill(navyblue)
    if pv:
        pygame.draw.rect(screen, orange, p)
    if ov:
        pygame.draw.rect(screen, white, o)
    pygame.display.flip()
