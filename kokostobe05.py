'''
This contains code from Attila Toth cocos2d Python series
Creating deifferent layers.

Check cocos2d   http://python.cocos2d.org/doc/api/cocos.sprite.html
for Changing sprites by way of actions
Parameters:
image (str, pyglet.image.AbstractImage or pyglet.image.Animation) – name of the image resource,
    a pyglet image or a pyglet animation
position (tuple[float]) – position of the anchor. Defaults to (0,0)
rotation (float) – the rotation (in degrees). Defaults to 0.
scale (float) – the zoom factor. Defaults to 1.
scale_x (float) – additional horizontal-only zoom factor. Defaults to 1.
scale_y (float) – additional vertical-only zoom factor. Defaults to 1.
opacity (int) – the opacity (0=transparent, 255=opaque). Defaults to 255.
color (tuple[int]) – the color to colorize the child (RGB 3-tuple). Defaults to (255,255,255).
anchor (tuple[float]) – (x, y) - point from where the image will be positioned, rotated and scaled in pixels.
     For example (image.width/2, image.height/2) is the center (default).

'''
import cocos
from cocos.director import director

class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        # Use kwargs to rescale your image.
        # In the next example the picture GDjmaHg.jpg has been
        # rescaled to 0.25 from the original size

        spr = cocos.sprite.Sprite("GDjmaHg.jpg", scale=0.25)


        spr.position = 400, 360

        self.add(spr)

class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super().__init__("spshipsprite.png")
        self.position = 740, 360



if __name__ == "__main__":
    director.init( width=1280, height=720,caption="Kokostobe05")

    spr1_layer = Sprite1()

    spr2_layer = Sprite2()




    test_scene = cocos.scene.Scene()
    test_scene.add(spr1_layer)
    test_scene.add(spr2_layer)

    director.run(test_scene)