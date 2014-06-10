
import renderer
import pygame as pg

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = renderer.Renderer('level.tmx')
        self.full_map = self.renderer.make_map()
        self.viewport = self.make_viewport(self.full_map)
        self.level_surface = self.make_level_surface(self.full_map)
        self.blockers = self.make_blockers('collision')
        
    def make_level_surface(self, full_map):
        map_rect = full_map.get_rect()
        map_width = map_rect.width
        map_height = map_rect.height
        size = map_width, map_height
        return pg.Surface(size).convert()
        
    def make_viewport(self, map_image):
        map_rect = map_image.get_rect()
        return self.screen.get_rect(bottom=map_rect.bottom)
        
    def render(self, screen):
        self.level_surface.blit(self.full_map, self.viewport, self.viewport)
        screen.blit(self.level_surface, (0,0), self.viewport)
        
    def make_blockers(self, blocker_name):
        blockers = pg.sprite.Group()
        for obj in self.renderer.tmx.getObjects():
            properties = obj.__dict__
            if properties['name'] == blocker_name:
                x = properties['x']
                y = properties['y']
                width = properties['width']
                height = properties['height']
                blocker = pg.sprite.Sprite()
                blocker.state = None
                blocker.rect = pg.Rect(x, y, width, height)
                blockers.add(blocker)
        return blockers
