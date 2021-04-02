#!/bin/bash
#find a random story to run
#cd into story directory and get complete path of one story dir
cd /home/pi/stories/scare-bear-stories
directory=ls | shuf -n 1
cd $(ls | shuf -n 1)
#$storyDir | cd
ls
#run the story
cp /home/pi/capstone/BearControl.py BearControl.py
python Main.py 

#update actions
rm BearControl.py
git pull
#cd into main git folder and pull to update
cd /home/pi/capstone
git pull
#now that we're all done, we can power off the pi safely
shutdown
