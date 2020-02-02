import pytmx
import os
import pygame as pg

class Renderer:
    #dir = os.path.join('resources', 'tmx')
    
    def __init__(self, filename):
        #self.tmx = pytmx.load_pygame(os.path.join(Renderer.dir, filename), pixelalpha=True)
        self.tmx = pytmx.load_pygame(filename, pixelalpha=True)
        self.size = self.tmx.width * self.tmx.tilewidth, self.tmx.height * self.tmx.tileheight

    def render(self, surface):
        tw = self.tmx.tilewidth
        th = self.tmx.tileheight
        gt = self.tmx.get_tile_image_by_gid
        if self.tmx.background_color:
            surface.fill(self.tmx.background_color)
        for layer in self.tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        surface.blit(tile, (x * tw, y * th))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                pass
            elif isinstance(layer, pytmx.TiledImageLayer):
                image = gt(layer.gid)
                if image:
                    surface.blit(image, (0, 0))

    def make_map(self):
        surf = pg.Surface(self.size)
        self.render(surf)
        return surf
