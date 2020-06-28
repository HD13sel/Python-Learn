#Is that Music
from pygame import mixer
mixer.init()
mixer.music.load('desafio21a.mp3')
mixer.music.play()
mixer.music.set_volume(35)
import time
time.sleep(360)
