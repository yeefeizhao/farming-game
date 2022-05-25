import pygame
from datetime import datetime

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cute kawaii farming simulator for asmr kindness and love")
bg = pygame.image.load("bg.png")
SCREEN.blit(bg, (0, 0))



def growPlant(num):

    return pygame.image.load("seed1\seed1-" + str(num) + ".png").convert_alpha()

def main():
    run = True
    player = pygame.image.load("char_walk_left.gif").convert_alpha()
    player_rect = player.get_rect(center = (400, 300))

    plant_left = pygame.image.load("seed1\seed1-1.png").convert_alpha()
    plant_right = pygame.image.load("seed1\seed1-1.png").convert_alpha()

    left_farm = pygame.Rect(40, 400, 160, 160)
    right_farm = pygame.Rect(240, 400, 160, 160)

    plant_left_counter = 1;
    plant_right_counter = 1;
    while run: 
         #this obj goes here and it swaps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            

            if keys[pygame.K_a]:
                player_rect.left -= 5
            if keys[pygame.K_w]:
                player_rect.top -= 5
            if keys[pygame.K_s]:
                player_rect.top += 5
            if keys[pygame.K_d]:
                player_rect.left += 5
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    plant_left = growPlant(plant_left_counter)
                    if plant_left_counter < 6:
                        plant_left_counter += 1
                    else:
                        plant_left_counter = 7
                if event.key == pygame.K_o:
                    plant_right = growPlant(plant_right_counter)
                    if plant_right_counter < 6:
                        plant_right_counter += 1
                    else:
                        plant_right_counter = 7
            
        SCREEN.blit(bg, (0,0))
        SCREEN.blit(plant_left, left_farm)
        SCREEN.blit(plant_right, right_farm)
        SCREEN.blit(player, player_rect)

        pygame.display.update()            
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()