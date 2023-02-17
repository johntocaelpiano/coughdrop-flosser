import pygame

class Bottom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((800, 10))
        self.image.fill((250,170,104))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 790
    
    def draw(self,surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))