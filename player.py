
import pygame as pg

class Player:
    def __init__(self, center):
        self.image = pg.Surface([50,50]).convert()
        self.color_init = (255,0,0)
        self.collision_color = (0,0,255)
        self.color = self.color_init
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=center)
        self.speed = 3
        
    def move(self, x, y):
        self.rect.x += x * self.speed
        self.rect.y += y * self.speed
        
    def update(self, keys, blocker):
        if keys[pg.K_UP]:
            self.move(0,-1)
        if keys[pg.K_DOWN]:
            self.move(0,1)
        if keys[pg.K_LEFT]:
            self.move(-1,0)
        if keys[pg.K_RIGHT]:
            self.move(1,0)
        
        if blocker:
            self.color = self.collision_color
        else:
            self.color = self.color_init
        
    def render(self, screen):
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
