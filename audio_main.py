import os, random, time, wave
import threading, keyboard
import multiprocessing
from audio_player import play_loop
from audio_recorder import AudioRecorder
from playsound import playsound

ar = AudioRecorder()

exit_event = threading.Event()
p = multiprocessing.Process(target=playsound, args=('audio_files/audio_001.wav',))

def play_loop():
    while True:
        files = os.listdir("audio_files/")
        file = random.choice(files)
        print(file)
        print(files)
        playsound("audio_files/"+file)
        if exit_event.is_set():
            print("breaking")
            break


def read_keystrokes():
    while True:
        key = keyboard.read_event()
        print(key)
        global p
        p.terminate()
        time.sleep(5)
        p = multiprocessing.Process(target=playsound, args=('audio_files/audio_001.wav',))
        p.start()
        #ar.record_audio()

#threading.Thread(target = play_loop).start()
threading.Thread(target = read_keystrokes).start()
if __name__ == '__main__':
    #time.sleep(1)
    p.start()

