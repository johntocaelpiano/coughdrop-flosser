import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("shooter_powerup.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += 15
        if self.rect.y >= 800:
            self.kill()