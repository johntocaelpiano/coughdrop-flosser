import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += 15
        if self.rect.y >= 800:
            self.kill()