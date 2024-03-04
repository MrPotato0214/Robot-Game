import pygame
import toolbox
import math
import random
from powerup import PowerUp
from explosion import Explosion

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, player):

        pygame.sprite.Sprite.__init__(self, self.containers)

        self.screen = screen
        self.x = x
        self.y = y
        self.player = player
        self.image = pygame.image.load("../assets/Enemy_04.png")
        self.image_hurt = pygame.image.load("../assets/Enemy_04Hurt.png")
        self.explosion_images = []
        self.explosion_images.append(pygame.image.load('../assets/MediumExplosion1.png'))
        self.explosion_images.append(pygame.image.load('../assets/MediumExplosion2.png'))
        self.explosion_images.append(pygame.image.load('../assets/MediumExplosion3.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 0.9
        self.health_max = 20
        self.health = self.health_max
        self.hurt_timer = 0
        self.damage = 1
        self.obsitcale_anger = 0
        self.obsticale_anger_max = 100
        self.health_bar_width = 35
        self.health_bar_height = 8
        self.health_bar_green = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.health_bar_red = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.hurt_timer = 0
        self.powerup_drop_chance = 99 # out of 100
        
       
    def update(self, projectiles, crates, explosions):
       
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)
        
        angle_rads = math.radians(self.angle)
        self.x_move = math.cos(angle_rads) * self.speed
        self.y_move = -math.sin(angle_rads) * self.speed
        test_rect = self.rect
        new_x = self.x + self.x_move
        new_y = self.y + self.y_move
        test_rect.center = (new_x, self.y)


        self.health_bar_red.x = self.rect.x
        self.health_bar_red.bottom = self.rect.y - 5
        pygame.draw.rect(self.screen, (255, 0, 0), self.health_bar_red)
        self.health_bar_green.topleft = self.health_bar_red.topleft
        health_percentage = self.health / self.health_max
        self.health_bar_green.width = self.health_bar_width * health_percentage
        pygame.draw.rect(self.screen, (0, 255, 0), self.health_bar_green)
        
        for crate in crates:
            if test_rect.colliderect(crate.rect):
                new_x = self.x
                self.getAngry(crate)

        test_rect.center = (self.x, new_y)
        for crate in crates:
            if test_rect.colliderect(crate.rect):
                new_y = self.y
                self.getAngry(crate)
        
        self.x = new_x
        self.y = new_y
        self.rect.center = (self.x, self.y)

        for explosion in explosions:
            if explosion.damage:
                if self.rect.colliderect(explosion.rect):
                    self.getHit(explosion.damage)

  
        
        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()

        if self.hurt_timer <= 0:
            image_to_rotate = self.image
        else:
            image_to_rotate = self.image_hurt
            self.hurt_timer -= 1
        
        image_to_draw, image_rect = toolbox.getRotatedImage(image_to_rotate, self.rect, self.angle)
        
        self.screen.blit(image_to_draw, image_rect)

    def getHit(self, damage):
        if damage:
            self.hurt_timer = 5
        self.x -= self.x_move * 10
        self.y -= self.y_move * 10
        self.health -= damage
        if self.health <= 0:
            self.health = 99999
            Explosion(self.screen, self.x, self.y, self.explosion_images, 5, 0, False)
            if random.randint(0, 100) < self.powerup_drop_chance:
                PowerUp(self.screen, self.x, self.y)
            self.kill()

    def getAngry(self, crate):
        self.obsitcale_anger += 1
        if self.obsitcale_anger >= self.obsticale_anger_max:
            crate.getHit(self.damage)
            self.obsitcal_anger = 0
        





    
     
