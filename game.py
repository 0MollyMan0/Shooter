import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        self.player = Player()
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        self.all_monsters.add(Monster())