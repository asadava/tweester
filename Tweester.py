#This is a Twister generator, click run and it will generate moves!
import random
import time

bodypartslist = ["left hand ", "right hand ", "left foot ", "right foot "]
colorslist = ["red", "yellow", "green", "blue"]

input("Welcome to Tweester, the Twister move generator! Press enter to continue.")
print("Generating moves...")
time.sleep(5)

while True:
    bodyparts = random.choice(bodypartslist)
    colors = random.choice(colorslist)
    print(bodyparts + colors)
    time.sleep(5)