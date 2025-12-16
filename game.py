import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def game_over(self):
        self.is_playing = False
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health

    def start(self):
        self.is_playing = True
        self.player.rect.x = 200
        self.player.rect.y = 500
        self.spawn_monster()
        self.spawn_monster()

    def update_game(self, screen):
        for projectile in self.player.all_projectiles:
            projectile.move()
    
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        screen.blit(self.player.image, self.player.rect)
        self.player.all_projectiles.draw(screen)
        self.player.update_health_bar(screen)
        self.all_monsters.draw(screen)

        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) and self.player.rect.x - 40 < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_a)) and self.player.rect.x > -40:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
