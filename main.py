import pygame
pygame.init()

pygame.display.set_caption("Shooter") # add a custom icon here in the future
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg') # change bg in the future

running = True

while running:

    screen.blit(background, (0, -200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()