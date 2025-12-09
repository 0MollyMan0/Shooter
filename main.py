import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Shooter") # add a custom icon here in the future
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    
    if (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d)) and game.player.rect.x - 40 < screen.get_width() - game.player.rect.width:
        game.player.move_right()
    elif (game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_a)) and game.player.rect.x > -40:
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False