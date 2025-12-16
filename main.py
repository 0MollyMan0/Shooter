import pygame
import math
from game import Game

pygame.init()

pygame.display.set_caption("Shooter") # add a custom icon here in the future
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('assets/bg.jpg')

banner_width, banner_height = 500, 500
banner = pygame.transform.scale(pygame.image.load('./assets/banner.png'), (banner_width, banner_height))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = 20

play_button_width, play_button_height = 400, 150
play_button = pygame.transform.scale(pygame.image.load('./assets/button.png'), (play_button_width, play_button_height))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33) + 10
play_button_rect.y = math.ceil(screen.get_height() / 2) + 30
game = Game()

clock = pygame.time.Clock()

running = True

while running:

    screen.blit(background, (0, -200))

    if game.is_playing:
        game.update_game(screen)
    else:
        screen.blit(play_button, play_button_rect)  
        screen.blit(banner, banner_rect)
        
    pygame.display.flip()
    clock.tick(60)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
    
