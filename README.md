# Simply
Just a python library created to a alternative from pygame

# how to use:
## create screen
to start, use
```python
window = simply.window(window,height,captions)
```

## drawing
with simply you can draw rectangles, squares, circles, and lines, lets try!

``` python
window.draw.rect(color, x, y, width, height, thickness) # rectangles and squares
window.draw.circle(color, x, y, radius, thickness) # circle
window.draw.line(color, sx, sy, ex, ey  thickness) # line
```

## clearing and showing
update to show the draw:

``` python
window.clear()
```

when you finish drawing you need to clear all with:
```python
window.clear()
```
## writting
``` python
window.draw.text(color, text, x, y, font, size)
```

## getting mouse position
when you `window.mouse_pos()` it returns a dictionary, example:
``` python
import simply as s

window = s.window(100,100,"mouse position")

while True:
    window.draw.text((255,255,255),str(window.mouse_pos()["x"])+str(window.mouse_pos()["y"]),0,0)
```
