import pygame 
import time
import BearControl as bc
#The pygame mixer module automatically runs the audio in the background!

# initalizes the various moving parts
pygame.mixer.init()
pygame.mixer.music.load("drip.ogg")

motors = bc.BearControl(mouthServoPin=26, neckServoPin=5)
motors.straighten_head()
motors.raise_fangs()

# start up the various functions
pygame.mixer.music.play()
print("done running all that boring setup stuff")
# This is where the actions will take place

#on wakerups
#21 - rotate
time.sleep(21)
motors.turn_head_backwards()
#29 - rotate back
time.sleep(8)
motors.straighten_head()
#70 - rotate
time.sleep(41)
motors.turn_head_backwards()
#72 rotate back
time.sleep(2)
motors.straighten_head()
#drip drip drip
#77 - shake
time.sleep(5)
motors.vibrate_head()
#punchline
#103 fangs out
time.sleep(24)
motors.lower_fangs()
#107 rotate head
time.sleep(4)
motors.turn_head_backwards()
#114 rotate back
time.sleep(7)
motors.straighten_head()
#124 shake
time.sleep(10)
motors.vibrate_head()
motors.straighten_head()
#126 
motors.raise_fangs()
#128 finish
time.sleep(2)
#cleanup
motors.halt()