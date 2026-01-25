import pygame
import random
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('./assets/comet.png')
        self.rect = self.image.get_rect()
        self.attack = 250
        self.velocity = random.uniform(3, 9)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 1800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
    
    def fall(self):
        self.rect.y += self.velocity

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.comet_event.game.player.damage(self.attack)
            self.remove()

        for monster in self.comet_event.game.check_collision(self, self.comet_event.game.all_monsters):
            monster.damage(self.attack)
            self.remove()

        if self.rect.y >= 530:
            self.remove()
        
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False