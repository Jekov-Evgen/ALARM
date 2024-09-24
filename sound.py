import pyglet
import sys


class SoundAlarm:
    def run_sound(self):
        song = pyglet.media.load('signal-elektronnogo-budilnika-33304.mp3')
        self.player = pyglet.media.Player()
        self.player.queue(song)
        self.player.play()
    
    
    def stop_sound(self):
        self.player.delete()
        sys.exit()