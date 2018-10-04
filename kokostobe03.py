'''
To customize the font in your text go to API cocos2d Python

http://python.cocos2d.org/doc/api/cocos.text.html

A few handy kwargs (Key words arguments, in red in your list of arguments for a function)

For pyglet 1.1.4 the available init keyword arguments are
font_name: Font family name(s); first matching is used
font_size: Font size, in points.
bold: bool
italic: bool
color : (int, int, int, int) or None
width: Width of the label in pixels, or None
height: Height of the label in pixels, or None
anchor_x: “left”, “center” or “right”
anchor_y: one of “bottom”, “baseline”, “center” or “top”
align : only when a width is supplied. One of “left”, “center”, “right”.
multiline : bool
dpi : Resolution of the fonts in this layout. Defaults to 96.


for 
color : (int, int, int, int) or None

the first three numbers are something between 0-255 (RGB), and the last number is the ALPHA -transparency
so think of your color as something like:
color=(RED,GREEN, BLUE, ALPHA)
Note
Check online for a code-colors list

'''
import cocos
from cocos.director import director

class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Who's afraid of Dragon's Tail?", font_name="mikado_outline_shadow", font_size=36,
                                 anchor_x="center", anchor_y="center", color=(255,255,0,255))
        label.position =640, 360
        self.add(label)





if __name__ == "__main__":
    director.init(width=1280, height=720,caption="Kokostobe03")




    hello_layer = HelloCocos()

    test_scene = cocos.scene.Scene(hello_layer)




    director.run(test_scene)
