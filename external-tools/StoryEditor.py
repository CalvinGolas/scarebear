import pygame
from pygame import mixer
import tkinter as tk
import os
# to deal with the offset we get from using get_pos, we add current time to the result we recieve
currentTime = 0
# make an array of tuples, first val = second time, second val = action

def play_audio():
    if not mixer.music.get_busy():
        mixer.music.play(start = currentTime)

def pause_audio():
    # if it's playing, pause it and store the value in the milliseconds counter
    if mixer.music.get_busy():
        mixer.music.pause()
        currentTime = mixer.music.get_pos() / 1000 + currentTime

def finish_editing():
    # upon exit, clear tuples with duplicate times
    # now create a main.python file and write the program to it
    pass

def back_ten_seconds():
    #can't go past ending
    pass

def forward_ten_seconds():
    # can't change value past zero


def load_sound_file():
    pass

def rotate_head_back():
    pass

def rotate_head_front():
    pass

def shake_head():
    pass

def raise_fangs():
    pass

def lower_fangs():
    pass

# initialize the app
root = tk.Tk()
root.title("Scare Bear Story Editor")
mixer.init()
audioStatus = tk.StringVar()
audioStatus.set("choosing")

# code for the buttons
# audio playback buttons
playButton = tk.Button(root, text = "play", command = play_audio)
playButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playButton.grid(row = 1, column = 1)

pauseButton = tk.Button(root, text = "pause", command = pause_audio)
pauseButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pauseButton.grid(row = 1, column = 2)

backTenSecondsButton = tk.Button(root, text = "go back ten sec", command = back_ten_seconds)
backTenSecondsButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
backTenSecondsButton.grid(row = 1, column = 0)

forwardTenSecondsButton = tk.Button(root, text = "skip forward ten sec", command = forward_ten_seconds)
forwardTenSecondsButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
forwardTenSecondsButton.grid(row = 1, column = 3)

# fang controls
raiseFangsButton = tk.Button(root, text = "add raise fangs cmd", command = raise_fangs)
raiseFangsButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
raiseFangsButton.grid(row = 2, column = 0)

lowerFangsButton = tk.Button(root, text = "add lower fangs cmd", command = lower_fangs)
lowerFangsButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
lowerFangsButton.grid(row = 2, column = 3)

# head rotation buttons
rotateHeadBackButton = tk.Button(root, text = "add rotate head back cmd", command = rotate_head_back)
rotateHeadBackButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
rotateHeadBackButton.grid(row = 3, column = 0)

shakeHeadButton = tk.Button(root, text = "add shake head cmd", command = shake_head)
shakeHeadButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
shakeHeadButton.grid(row = 4, column = 0)

rotateHeadForwardButton = tk.Button(root, text = "add rotate head forward cmd", command = rotate_head_back)
rotateHeadForwardButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
rotateHeadForwardButton.grid(row = 3, column = 3)

# button to finish editing
finishEditingButton = tk.Button(root, text = "finish and upload", command = finish_editing)
finishEditingButton.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
finishEditingButton.grid(row = 5, column = 0)



tk.mainloop()