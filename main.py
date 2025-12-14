import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Shooter") # add a custom icon here in the future
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('assets/bg.jpg')

banner_width, banner_height = 500, 500
banner = pygame.transform.scale(pygame.image.load('./assets/banner.png'), (banner_width, banner_height))
banner_x = screen_width / 2 - banner_width / 2
banner_y = (screen_height / 2 - banner_height / 2) - 80

play_button_width, play_button_height = 400, 150
play_button = pygame.transform.scale(pygame.image.load('./assets/button.png'), (play_button_width, play_button_height))
play_button_x = (screen_width / 2 - play_button_width / 2) + 10
play_button_y = banner_height - 50

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    if game.is_playing:
        game.update_game(screen)
    else:
        screen.blit(banner, (banner_x, banner_y))
        screen.blit(play_button, (play_button_x, play_button_y))      

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v or event.key == pygame.K_SPACE:
                game.player.lauch_projectile()
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False