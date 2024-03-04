import pygame
import random
from player import Player
from projectile import WaterBallon
from enemy import Enemy
from crate import Crate
from crate import ExplosiveCrate
from explosion import Explosion
from powerup import PowerUp



# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock() 
running = True

#Creat back ground image
background_image = pygame.image.load("../assets/BG_Grass.png")

playerGroup = pygame.sprite.Group()
projectileGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
cratesGroup = pygame.sprite.Group()
explosionsGroup = pygame.sprite.Group()
powerupGroup = pygame.sprite.Group()

Player.containers = playerGroup
WaterBallon.containers = projectileGroup
Enemy.containers = enemiesGroup
Crate.containers = cratesGroup
Explosion.containers = explosionsGroup
PowerUp.containers = powerupGroup

enemy_spawn_timer_max = 80
enemy_spawn_timer = 0

#Add the conditions for player

mr_player = Player(screen, 100, 200)

for i in range(0, 10):
    ExplosiveCrate(screen, random.randint(0, game_width), random.randint(0, game_height), mr_player)
    Crate(screen, random.randint(0, game_width), random.randint(0, game_height), mr_player)
    

# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # add movement to my player        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mr_player.move(1,0, cratesGroup)
    if keys[pygame.K_a]:
        mr_player.move(-1,0, cratesGroup)
    if keys[pygame.K_s]:
        mr_player.move(0,1, cratesGroup)
    if keys[pygame.K_w]:
        mr_player.move(0,-1, cratesGroup)
    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()
    if keys[pygame.K_SPACE]:
        mr_player.placeCrate()
    if pygame.mouse.get_pressed()[2]:
        mr_player.placeExplosiveCrate()

    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        new_enemy = Enemy(screen, 0, 0, mr_player)
        side_to_spawn = random.randint(0, 3)
        if side_to_spawn == 0:
            new_enemy.x = random.randint(0, game_width)
            new_enemy.y = -new_enemy.image.get_height()
        elif side_to_spawn == 1:
            new_enemy.x = random.randint(0, game_width)
            new_enemy.y = game_height + new_enemy.image.get_height()
        elif side_to_spawn == 2:
            new_enemy.x = -new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        elif side_to_spawn == 3:
            new_enemy.x = game_width + new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        enemy_spawn_timer = enemy_spawn_timer_max
    
    
 #blit the background(fully make the background)
    screen.blit(background_image, (0, 0))
    
 #update the player
    
    for powerup in powerupGroup:
        powerup.update(mr_player)

    for explosion in explosionsGroup:
        explosion.update()


    for projectile in projectileGroup:
        projectile.update()


    for enemy in enemiesGroup:
        enemy.update(projectileGroup, cratesGroup, explosionsGroup)

    for crate in cratesGroup:
        crate.update(projectileGroup, explosionsGroup)

   
    
    mr_player.update(enemiesGroup, explosionsGroup)
    
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
