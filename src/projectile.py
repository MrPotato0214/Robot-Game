import pygame
import toolbox
import math
from explosion import Explosion

class WaterBallon(pygame.sprite.Sprite):
    
    def __init__(self, screen, x, y, angle):
        #make ballon sprite
        pygame.sprite.Sprite.__init__(self, self.containers)
        #var
        self.screen = screen
        self.angle = angle
        self.angle_rads = math.radians(self.angle)
        self.y = y
        self.x = x
        self.image = pygame.image.load("../assets/BalloonSmall.png")
        self.explsion_images = []
        self.explsion_images.append(pygame.image.load("../assets/SplashSmall1.png"))
        self.explsion_images.append(pygame.image.load("../assets/SplashSmall2.png"))
        self.explsion_images.append(pygame.image.load("../assets/SplashSmall3.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.speed = 10
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.damage = 6 

    def update(self):
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)
        is_off_screen = self.x < -self.image.get_width() or self.x > self.screen.get_width() + self.image.get_width() or self.y < -self.image.get_height() or self.y > self.screen.get_height() + self.image.get_height()

        # remove balloon if its to far of the screeen
        if is_off_screen:
            self.kill()
        
        self.screen.blit(self.image, self.rect)

    def explode(self):
        Explosion(self.screen, self.x, self.y, self.explsion_images, 5, 0, False)
        self.kill()



class SplitWaterBallon(WaterBallon):
    def __init__(self, screen, x, y, angle):
        WaterBallon.__init__(self,screen, x, y, angle)
        self.image = pygame.image.load("../assets/BalloonSmallGreen.png")
        self.damage = 7
        self.rect = self.image.get_rect()
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)


class WaterDroplet(WaterBallon):
    def __init__(self, screen, x, y, angle):
        WaterBallon.__init__(self, screen, x, y, angle)
        self.image = pygame.image.load("../assets/DropSmall.png")
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.damage = 3

class ExplosiveWaterBallon(WaterBallon):
     def __init__(self, screen, x, y, angle):
        WaterBallon.__init__(self, screen, x, y, angle)
        self.image = pygame.image.load("../assets/Balloon.png")
        self.rect = self.image.get_rect()
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.explsion_images = []
        self.explsion_images.append(pygame.image.load("../assets/SplashLarge1.png"))
        self.explsion_images.append(pygame.image.load("../assets/SplashLarge2.png"))
        self.explsion_images.append(pygame.image.load("../assets/SplashLarge3.png"))
     def explode(self):
        Explosion(self.screen, self.x, self.y, self.explsion_images, 5, 2, False)
        self.kill()


    
         







        
        
        
        
        
