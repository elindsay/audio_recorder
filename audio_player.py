import os, random, time, wave
from playsound import playsound

def play_loop():
    while True:
        print("in play loop")
        files = os.listdir("audio_answers/")
        file = random.choice(files)
        print(file)
        print(files)
        playsound("audio_answers/"+file)

