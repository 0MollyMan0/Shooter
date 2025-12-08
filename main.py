import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 5
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

pygame.display.set_caption("Shooter") # add a custom icon here in the future
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

player = Player()

running = True

while running:

    screen.blit(background, (0, -200))

    screen.blit(player.image, player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()