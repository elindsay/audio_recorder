import threading, keyboard
from audio_player import play_loop
from audio_recorder import AudioRecorder

ar = AudioRecorder()

def read_keystrokes():
    while True:
        key = keyboard.read_event()
        print(key)
        ar.record_audio()

threading.Thread(target = play_loop).start()
threading.Thread(target = read_keystrokes).start()

