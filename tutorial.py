# form_str = '{:04d}'.format(25)
# form_str2 = '{0:02d}'.format(4)
# print(form_str)
# print(form_str2)
# print(len(form_str2))
from os import path
from vlc import MediaPlayer
from time import sleep

music_path = path.dirname(__file__)+'/alarm.mp3'
music_proc = MediaPlayer(music_path)
music_proc.play()
while True:
    if input('e -exit ') == 'e':
        music_proc.stop()
        break
