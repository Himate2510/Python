import pygame, random
pygame.init()
bgcolor = (0,0,0)
clock = pygame.time.Clock()
blue = pygame.Color("Blue")
white = pygame.Color("White")
red = pygame.Color("Red")
black = pygame.Color("Black")
navyblue = pygame.Color("Navy")
yellow = pygame.Color("Yellow")
sprite1 = pygame.USEREVENT + 1
bg = pygame.USEREVENT + 2
class Sprite(pygame.sprite.Sprite) :
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boun = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            boun = True
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            boun = True
            self.velocity[1] = -self.velocity[1]
        if boun:
            pygame.event.post(pygame.event.Event(sprite1))
            pygame.event.post(pygame.event.Event(bg))
    def changesc(self) :
        self.image.fill(random.choice([white,yellow,black]))
def changebg() :
    global bgcolor
    bgcolor = random.choice([blue,red,navyblue])
all = pygame.sprite.Group()
obj1 = Sprite(white,50,50)
obj1.rect.x = random.randint(0,480)
obj1.rect.y = random.randint(0,350)
all.add(obj1)
screen = pygame.display.set_mode((500,500))
screen.fill(bgcolor)
t = True
while t :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            pygame.quit()
        elif e.type == sprite1 :
            obj1.changesc()
        if e.type == bg :
            changebg()
    all.update()
    screen.fill(bgcolor)
    all.draw(screen)
    pygame.display.flip()
    clock.tick(999)