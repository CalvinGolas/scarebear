import pygame 
import time
import BearControl
#The pygame mixer module automatically runs the audio in the background!

# initalizes the various moving parts
pygame.mixer.init()
pygame.mixer.music.load("widemouth.ogg")

motors = BearControl.BearControl(26, 5)


# start up the various functions
pygame.mixer.music.play()
print("done running all that boring setup stuff")
time.sleep(20)