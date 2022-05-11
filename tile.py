import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class TileMap():
    def __init__(self, filename):
        self.tile_size = 16
        self.start.x = 0
        self.start.y = 0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def readcsv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimeter=',')
            for row in data: 
                map.append(list(row))
        return map