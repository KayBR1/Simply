# Simply
a thin layer of simplicity over pygame

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
window.update()
```

when you finish drawing you need to clear all with:
```python
window.clear()
```

please put `quit()` command on your loop

## writting
``` python
window.draw.text(color, text, x, y, font, size)
```

## user input(1.1.0 feature)
when you `window.mouse_pos()` it returns a dictionary, example:
``` python
import simply as s

window = s.window(100,100,"mouse position")

while True:
   window.draw.text((255,255,255),str(window.mouse_pos()["x"])+", "+str(window.mouse_pos()["y"]),0,0)
```

you can get key pressing with `window.input.key_down(key)`
``` python
print("press key A")
while True:
   quit()
   if window.input.key_down("K_A"):
      window.draw.text((255,255,255),"key A pressed!",0,0)
      sleep(0.5)
   window.update()
   window.clear()
```

and you can get mouse pressing with `mouse_down()`

## images and sound(1.1.0 features)
to play sound use `window.sound(path)` and to display images use `window.draw.image(path, x, y, width, height, angle)`