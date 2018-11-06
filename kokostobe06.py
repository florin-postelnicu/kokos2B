
import cocos
from cocos.director import director
import pyglet


class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        img = pyglet.image.load("spritesheet1.jpg")
        img_grid = pyglet.image.ImageGrid(img, 2, 8, item_width=50, item_height=55)
       

        anim = pyglet.image.Animation.from_image_sequence(img_grid, 0.1, loop=True)
        spr = cocos.sprite.Sprite(anim, scale=3)
        spr.position = 200, 500
        self.add(spr)






class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super().__init__("spshipsprite.png")
        self.position = 640, 360


if __name__=="__main__":
    director.init(width=1280, height=720, caption="WINDOW")
    director.window.pop_handlers()
    spr1_layer = Sprite1()
    spr2_layer = Sprite2()

    test_scene = cocos.scene.Scene()
    test_scene.add(spr1_layer, z=1)
    test_scene.add(spr2_layer, z=2)

    director.run(test_scene)
