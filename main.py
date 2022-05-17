import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from player import *

'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def moveRight(self):
        self.rect.x += 10
    def moveLeft(self):
        self.rect.x -= 10
    def moveUp(self):
        self.rect.y -= 10
    def moveDown(self):
        self.rect.y += 10
'''

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cute kawaii farming simulator for asmr kindness and love")
bg = pygame.image.load("bg.png")
SCREEN.blit(bg, (0, 0))



def growPlant():
    pass



def main():
    run = True
    player = pygame.image.load("char_walk_left.gif")
    player_x = 0
    player_y = 0

    while run: 
         #this obj goes here and it swaps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x += -10
                if event.key == pygame.K_RIGHT:
                    player_x += 10
                if event.key == pygame.K_UP:
                    player_y += -10
                if event.key == pygame.K_DOWN:
                    player_y += 10
                if event.key == pygame.K_f:
                    growPlant()
        

        SCREEN.blit(bg, (0,0))
        SCREEN.blit(player, (player_x, player_y))

        pygame.display.update()            
        clock.tick(15)
    
    pygame.quit()

if __name__ == "__main__":
    main()