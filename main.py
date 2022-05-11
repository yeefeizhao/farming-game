import pygame
from pytmx.util_pygame import load_pygame
from player import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.image.load('char_walk_left.gif') 
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 320, 240
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FARMING")
tmx_data = load_pygame('final_project_map.tmx')
player = pygame.image.load('char_walk_left.gif')
rect = player.get_rect()

def main():
    run = True
    for layer in tmx_data.visible_layers:
        for x, y, gid in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile != None:
                SCREEN.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    pygame.display.update()
    #i like men - dshi

    while run: 
        SCREEN.blit(player, (5,5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
                
    clock.tick(60)
        

if __name__ == "__main__":
    main()


