#
# cocos2d
# http://cocos2d.org
#

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet import image, font
from pyglet.gl import *
from pyglet.window import key

from cocos.actions import *
from cocos.director import director
from cocos.layer import * 
from cocos.scene import Scene
from cocos.sprite import Sprite


class FontLayer( Layer ):
    def __init__( self ):
        super( FontLayer, self ).__init__()

        self.batch = pyglet.graphics.Batch()

        self.text_title = pyglet.text.Label("Blending and filtering demo",
            font_size=32,
            x=5,
            y=director.get_window_size()[1],
            anchor_x=font.Text.LEFT,
            anchor_y=font.Text.TOP,
            batch=self.batch)

    def draw( self ):
        super( FontLayer, self).draw()
        self.batch.draw()


class SpriteLayer( Layer ):

    is_event_handler = True     #: enable pyglet's events

    def __init__( self, index=1 ):
        super(SpriteLayer, self ).__init__()
        self.index = index

        self.image = pyglet.resource.image('grossini.png')

        self.sprite1 = Sprite(self.image, blend_mode=Sprite.BLEND_STANDARD)
        self.sprite1.x = director.get_window_size()[0] / 2 - 100
        self.sprite1.y = director.get_window_size()[0] / 2
        self.add( self.sprite1 )

        self.sprite2 = Sprite(self.image, blend_mode=Sprite.BLEND_ADDITIVE)
        self.sprite2.x = director.get_window_size()[0] / 2 + 100
        self.sprite2.y = director.get_window_size()[0] / 2
        self.add( self.sprite2 )

        self.sprite3 = Sprite(self.image, blend_mode=Sprite.BLEND_STANDARD, filter_mode=Sprite.FILTER_NONE)
        self.sprite3.x = director.get_window_size()[0] / 2 - 100
        self.sprite3.y = director.get_window_size()[0] / 2 - 150
        self.add( self.sprite3 )

        self.sprite4 = Sprite(self.image, blend_mode=Sprite.BLEND_ADDITIVE, filter_mode=Sprite.FILTER_NONE)
        self.sprite4.x = director.get_window_size()[0] / 2 + 100
        self.sprite4.y = director.get_window_size()[0] / 2 - 150
        self.add( self.sprite4 )

    def on_key_release( self, keys, mod ):
        # LEFT: go to previous scene
        # RIGTH: go to next scene
        # ENTER: restart scene
        if keys == key.LEFT:
            self.index -= 1
            if self.index < 1:
                self.index = len( tests )
        elif keys == key.RIGHT:
            self.index += 1
            if self.index > len( tests ):
                self.index = 1

        if keys in (key.LEFT, key.RIGHT, key.ENTER):
            director.replace( get_sprite_test( self.index ) )
            return True


if __name__ == "__main__":
    director.init( resizable=True, caption='Cocos - Blending demo' )
    director.run( Scene(ColorLayer(96, 0, 128, 255), FontLayer(), SpriteLayer()) )

