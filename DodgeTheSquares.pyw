import sys, os, pygame, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Game heehee")
screen = pygame.display.set_mode((1280, 720))

playerPos = [610, 536]

enemies = []
enemyCounter = 0
enemyDelay = 1000

score = 0

gameLoop = True

while gameLoop:
    for e in pygame.event.get():
        if e.type == QUIT: sys.exit()
    
    if pygame.time.get_ticks() % 1000 == 0: score += 1
    
    playerPos[0] = round(pygame.mouse.get_pos()[0]-32)
    
    enemyCounter += 1
    if enemyCounter >= enemyDelay:
        enemies.append([random.randint(0, 1216), -64])
        enemyCounter = 0
        if enemyDelay > 30: enemyDelay -= 10
    
    for i in range(len(enemies)-1, -1, -1):
        enemies[i][1] += 0.5
        if enemies[i][1] + 64 >= 600:
            del enemies[i]
            continue
        if pygame.Rect.colliderect(pygame.Rect(playerPos[0], playerPos[1], 64, 64), pygame.Rect(enemies[i][0], enemies[i][1], 64, 64)):
            gameLoop = False
    
    screen.fill((60, 140, 200))
    
    pygame.draw.rect(screen, (50, 120, 60), (0, 600, 1280, 120))
    for enemy in enemies:
        pygame.draw.rect(screen, (200, 20, 10), (enemy[0], round(enemy[1]), 64, 64))
    pygame.draw.rect(screen, (180, 180, 200), (playerPos[0], playerPos[1], 64, 64))
    
    font = pygame.font.SysFont("Comic Sans MS", 60)
    img = font.render("Score: " + str(score), True, (180, 180, 200))
    imgRect = img.get_rect()
    imgRect.center = [640, 660]
    screen.blit(img, imgRect)
    
    pygame.display.update()

screen.fill((20, 20, 20))

font = pygame.font.SysFont("times", 80)
img = font.render("YOU DIED", True, (120, 0, 0))
imgRect = img.get_rect()
imgRect.h = imgRect.h * 1.5
img = pygame.transform.scale(img, (imgRect.w, imgRect.h))
imgRect.center = [640, 360]
screen.blit(img, imgRect)

font = pygame.font.SysFont("Comic Sans MS", 20)
img = font.render("Final Score: " + str(score), True, (120, 10, 20))
imgRect = img.get_rect()
imgRect.center = [640, 420]
screen.blit(img, imgRect)

pygame.display.update()

while 1:
    for e in pygame.event.get():
        if e.type == QUIT: sys.exit()
