import pygame as pg

pg.init()

# def color object
colors = {
"red": (255,0,0),
"orange": (255,150,0),
"yellow": (255,255,0),
"limr": (175,255,0),
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

# automatic quit detection
def quit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

# class windoe
class Window:
    def __init__(self, width: int = 100, height: int = 100, caption: str = "") -> None:
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)
        self.draw = self.Draw(self)
        self.input = self.Input(self)

    def update(self) -> None:
        pg.display.update()

    def clear(self, color=(0,0,0)) -> None:
        self.screen.fill(color)

    def sound(self, path):
        pg.mixer.Sound(path).play()

    # input
    class Input:
        def __init__(self, window):
            self.window = window
        # key detection
        def key_down(self, key) -> bool:
            return pg.key.get_pressed[key]

        # mouse down
        def mouse_down(self) -> bool:
            return pg.MOUSEBUTTONDOWN in pg.event.get().type
        # mouse posiito 
        def mouse_pos(self) -> dict:
            return {
            "x": pg.mouse.get_pos()[0],
            "y": pg.mouse.get_pos()[1]
            }
    class Draw:
        def __init__(self, window):
            self.window = window

        # circle drawing
        def circle(self, color, x:float, y:float, radius:float, thickness:float=0) -> None:
            pg.draw.circle(self.window.screen, color, (x, y), radius, thickness)

        # rect drawing
        def rect(self, color, x:float, y:float, width:float, height:float, thickness:float=0) -> None:
            pg.draw.rect(self.window.screen, color, (x, y, width, height),thickness)

        # line drawing
        def line(self, color, xs:float, ys:float, xe:float, ye:float, thickness:float=10) -> None:
            pg.draw.line(self.window.screen, color, (xs, ys), (xe,ye), thickness)

        # writting
        def text(self, color, text:str, x:float, y:float, font:str="arial", size:float=100) -> None:
            self.window.screen.blit(pg.font.SysFont(font,size,True,False).render(text,False,color),(x,y))

        # image rendering
        def image(self, path:str, x:float, y:float, width:float=1, height:float=1, angle:int=0) -> None:
            image = pg.image.load(path)
            resized = pg.transform.scale_by(image, (width, height))
            rotated = pg.transform.rotate(resized, -angle)
            self.window.screen.blit(rotated,(x,y))
