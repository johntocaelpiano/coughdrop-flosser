import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
    
        self.image =pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
    
    def update(self):
        self.rect.y += 12
        if self.rect.y >=800:
            self.kill()