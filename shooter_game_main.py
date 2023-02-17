import pygame
import random
from shooter_game_player import Player
from shooter_game_bullets import Bullet
from shooter_game_target import Target 
from shooter_game_border import Bottom
from shooter_game_powerup import Powerup
from shooter_game_lifeup import Lifeup

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Shooter Game")

def main():
    p1 = Player()
    b1 = Bottom()
    bullet_group = pygame.sprite.Group()
    shoot = False
    cooldown = 0
    score  = 0
    health = 10
    target_group = pygame.sprite.Group()
    powerupgroup = pygame.sprite.Group()
    lifeupgroup = pygame.sprite.Group()
    white = (255, 255, 255)
    font =  pygame.font.SysFont("Century Gothic", 30, True)
    game_over = False

    for target in range(200):
        target = Target(random.randint(0,800), random.randint(-100000,0))
        target_group.add(target)

    for powerup in range(10):
        powerup = Powerup(random.randint(0,800), random.randint(-100000, 0))
        powerupgroup.add(powerup)
    
    for lifeup in range(10):
        lifeup = Lifeup(random.randint(0,800), random.randint(-100000, 0))
        lifeupgroup.add(lifeup)
    
    cooldown_limit = 10

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot = False

        p1.handle_keys()
        bullet_group.update()
        target_group.update()
        powerupgroup.update()  
        lifeupgroup.update()

        score_text = font.render(f"Score: {score}", True, white)
        health_text = font.render(f"Health: {health}", True, white)

        if cooldown > 0:
            cooldown -= 1

        if shoot:
            if cooldown == 0:               
                cooldown = cooldown_limit
                bullet = Bullet(p1.rect.centerx, p1.rect.centery)
                bullet_group.add(bullet)
                
        if pygame.sprite.groupcollide(bullet_group, target_group, True, True):
            score += 1

        if pygame.sprite.spritecollide(b1, target_group, True):
            health -= 1
        
        if pygame.sprite.spritecollide(p1, powerupgroup, True):
            cooldown_limit -=2
        
        if pygame.sprite.spritecollide(p1, lifeupgroup, True):
            health += 1

        if health == 0:
            game_over = True
        
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_over = False
                        health = 10
                        main()
            screen.fill((255,100,100))
            game_over_font = pygame.font.SysFont("Century Gothic", 70, True)
            game_over_text = game_over_font.render("Game Over", True, white)
            play_again_text = font.render("Play again? Press Space", True, white)
            final_score_text = font.render(f"Final Score: {score}", True, white)
            screen.blit(game_over_text, (10, 330))
            screen.blit(play_again_text, (10, 530))
            screen.blit(final_score_text, (10, 430))
            pygame.display.update()
            



        screen.fill((250,170,104))
        bullet_group.draw(screen)
        p1.draw(screen)
        b1.draw(screen)
        target_group.draw(screen)
        powerupgroup.draw(screen)
        lifeupgroup.draw(screen)

        screen.blit(score_text, (30, 30))
        screen.blit(health_text, (600, 30))

        pygame.display.update()
        clock.tick(30)

main()
pygame.quit()
quit()  