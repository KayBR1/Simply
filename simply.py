import pygame as pg

pg.init()

colors = {
"red": (255,0,0),
"orange": (255,150,0),
"yellow": (255,255,0),
"lime": (175,255,0),
"green": (0,255,0),
"sea": (0,255,175),
"cyan": (0,255,255),
"blue": (0,0,255),
"purple":  (175,0,255),
"lilac": (255,0,255),
"magenta": (255,0,175),
"vine": (100,0,0),
"brown": (150,50,0),
"pink": (255,150,255),
"white": (255,255,255),
"black": (0,0,0)
}

def quit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

class Window:
    def __init__(self, width: int = 100, height: int = 100, caption: str = "") -> None:
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)
        self.draw = self.Draw(self)

    def update(self) -> None:
        pg.display.update()

    def clear(self, color=(0,0,0)) -> None:
        self.screen.fill(color)

    def play_sound(self, path):
        pg.mixer.Sound(path).play()

    def key_down(self, key):
        return pg.key.get_pressed[key]
    def event(self, event:str) -> bool:
        for e in pg.event.get():
            return e.type == event

    def mouse_pos(self) -> dict:
        return {
        "x": pg.mouse.get_pos()[0],
        "y": pg.mouse.get_pos()[1]
        }
    class Draw:
        
        def __init__(self, window):
            self.window = window

        def circle(self, color, x:float, y:float, radius:float, thickness:float=0) -> None:
            pg.draw.circle(self.window.screen, color, (x, y), radius, thickness)

        def rect(self, color, x:float, y:float, width:float, height:float, thickness:float=0) -> None:
            pg.draw.rect(self.window.screen, color, (x, y, width, height),thickness)

        def line(self, color, xs:float, ys:float, xe:float, ye:float, thickness:float=10) -> None:
            pg.draw.line(self.window.screen, color, (xs, ys), (xe,ye), thickness)

        def text(self, color, text:str, x:float, y:float, font:str="arial", size:float=100) -> None:
            self.window.screen.blit(pg.font.SysFont(font,size,True,False).render(text,False,color),(x,y))

        def image(self, path:str, x:float, y:float) -> None:
            self.window.screen.blit(pg.image.load(path).convert_alpha(),(x,y))
