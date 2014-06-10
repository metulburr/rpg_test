
import pygame as pg
import player
import level
        
class Control:
    def __init__(self):
        pg.init()
        self.screensize = (480,480)
        self.screen = pg.display.set_mode(self.screensize)
        self.screenrect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        
        self.level = level.Level(self.screen)
        self.player = player.Player(self.screenrect.center)
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
                
    def update(self):
        self.keys = pg.key.get_pressed()
        blocker = pg.sprite.spritecollideany(self.player, self.level.blockers)
        self.player.update(self.keys, blocker)
        
    def render(self):
        self.screen.fill((0,0,0))
        self.level.render(self.screen)
        self.player.render(self.screen)
        
    def run(self):
        while not self.done:
            self.events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            pg.display.update()
            
app = Control()
app.run()
