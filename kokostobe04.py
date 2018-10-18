'''
Using default handlers

Go to cocos2d Programming Guide
and check:
 Default Handlers


 Find the keys (short cuts) to manage the screen.
CTRL + f

Toggles fullscreen mode

CTRL + s

Takes a screenshot of the current window.

A file named ‘screenshot-xxxxx’ will be saved in the current working directory.

CTRL + p

Toggles Pause

CTRL + w

Toggles wire-frame mode

CTRL + x

Toggles FPS display

CTRL + i

Toggles the built-in python interpreter
'''
import cocos
from cocos.director import director

class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Who's afraid of Dragon's Tail?",
                                 font_name="mikado_outline_shadow",
                                 bold=True,
                                 italic=True ,font_size=36,
                                 anchor_x="center", anchor_y="center",
                                 color=(255,255,0,255), dpi = 120)
        size = director.get_window_size()
        label.position = size[0]/2, size[1]/2
        self.add(label)

if __name__ == "__main__":
    director.init( width=1280, height=720,caption="Kokostobe03")

    # If you want to remove the default handlers use the command :
    # director.window.pop_handlers()

    hello_layer = HelloCocos()
    test_scene = cocos.scene.Scene(hello_layer)
    director.run(test_scene)