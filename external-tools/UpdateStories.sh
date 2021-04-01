#find a random story to run
#TODO: cd into story directory and get complete path of one story dir
storyDir= ls -d $PWD/* | shuf -n 1
#run the story
cd $storyDir
cp $ #TODO: value of bearcontrol.py bearcontrol.py
python main.py 

#update actions
rm bearcontrol.py
git pull
#TODO: cd into main git folder and pull to update
git pull
#now that we're all done, we can power off the pi safely
shutdown