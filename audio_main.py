import os, random, time, wave
import threading
import keyboard
import multiprocessing
from audio_player import play_loop
from audio_recorder import AudioRecorder
from playsound import playsound
import RPi.GPIO as GPIO

ar = AudioRecorder()

p = multiprocessing.Process(target=play_loop)

def read_keystrokes():
    while True:
        key = keyboard.read_event()
        print(key)
        global p
        p.terminate()
        time.sleep(1)
        #p = playsound("audio_questions/question.wav")
        p = multiprocessing.Process(target=playsound, args=("audio_questions/question.wav",))
        p.start()
        time.sleep(4)
        p.terminate()
        ar.record_audio()
        time.sleep(1)
        print("here 1")
        p = multiprocessing.Process(target=play_loop)
        p.start()
        print("here 3")


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

ar = AudioRecorder()

def read_gpio():
    last_state = GPIO.input(18)
    while True:
        state = GPIO.input(18)
        if(last_state != state):
            last_state = state
            print("Button pushed") 
            global p
            p.terminate()
            playsound("audio_questions/question.wav")
            ar.record_audio()
            p = multiprocessing.Process(target=play_loop)
            p.start()
            ar.record_audio()

#threading.Thread(target = play_loop).start()
threading.Thread(target = read_keystrokes).start()
#threading.Thread(target = read_gpio).start()
if __name__ == '__main__':
    #time.sleep(1)
    p.start()

