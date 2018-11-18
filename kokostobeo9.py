'''
The background is a map created with Tiled Map Editor,
model2.tmx
The map is saved as a CSV file.
The layers in the map can be accessed through their names ; "ground", "trees", "water"

'''



import cocos
from cocos.director import director
import pyglet
from pyglet.window import key


class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT]- keyboard[key.LEFT])*500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN])*500
        self.target.velocity = (vel_x , vel_y)
        scroller.set_focus(self.target.x, self.target.y)




class UfoLayer(cocos.layer.ScrollableLayer):
    def __init__(self):
        super().__init__()
        img = pyglet.image.load("res/rob2.png")
        img_grid = pyglet.image.ImageGrid(img, 6, 9, item_width= 64, item_height= 64)
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)
        spr = cocos.sprite.Sprite(anim)
        spr.position = 200, 500
        spr.velocity = (0,0)
        spr.do(Mover())
        self.add(spr)





class BackgroundLayer():
    def __init__(self):
        bg = cocos.tiles.load("res/model2.tmx")
        self.layer1 = bg["ground"]
        self.layer2 = bg["trees"]
        self.layer3 = bg["water"]

        #
        # self.px_width = bg.width
        # 
        # self.px_height = bg.height
        #
        # self.add(bg)







if __name__=="__main__":
    director.init(width=1280, height=720, caption="WINDOW")
    director.window.pop_handlers()

    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)


    ufo_layer = UfoLayer()

    bg_layer = BackgroundLayer()

    scroller = cocos.layer.ScrollingManager()


    scroller.add(bg_layer.layer1)
    scroller.add(bg_layer.layer2)
    scroller.add(bg_layer.layer3)

    scroller.add(ufo_layer)


    test_scene = cocos.scene.Scene()
    test_scene.add(scroller)


    director.run(test_scene)
