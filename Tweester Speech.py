import random
import time
import os
from gtts import gTTS

bodypartslist = ["Left hand ", "Right hand ", "Left foot ", "Right foot "]
colorslist = ["red", "yellow", "green", "blue"]

input("Welcome to Tweester, the Twister move generator! Press enter to continue.")
print("Generating moves...")
time.sleep(5)

while True:
    text = random.choice(bodypartslist) + random.choice(colorslist)
    tts = gTTS(text, tld='com')
    tts.save("move.wav")
    os.system("move.wav")
    print(text)
    time.sleep(5)
    os.remove("move.wav")