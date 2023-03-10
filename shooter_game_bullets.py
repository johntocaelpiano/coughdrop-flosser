import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
    
        self.image =pygame.Surface((10,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y -= 10
        if self.rect.y <= 0:
            self.kill() 