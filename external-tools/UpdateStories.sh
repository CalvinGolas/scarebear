#find a random story to run
#cd into story directory and get complete path of one story dir
cd /home/pi/stories/scare-bear-stories
storyDir= ls -d $PWD/* | shuf -n 1
#run the story
cd $storyDir
cp $ ../../capstone/bearcontrol.py bearcontrol.py
python Main.py 

#update actions
rm bearcontrol.py
git pull
#cd into main git folder and pull to update
cd ../../capstone
git pull
#now that we're all done, we can power off the pi safely
shutdown
