import pygame
pygame.init()

pygame.display.set_caption("Shooter") # add a custom icon here in the future
pygame.display.set_mode((500, 300))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()