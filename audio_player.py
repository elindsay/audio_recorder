import os, random, time, wave
from playsound import playsound

def play_loop():
    while True:
        files = os.listdir("audio_answers/")
        file = random.choice(files)
        print(file)
        print(files)
        playsound("audio_answers/"+file)
