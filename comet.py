import pygame
import random
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('./assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.uniform(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
    
    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 530:
            self.remove()