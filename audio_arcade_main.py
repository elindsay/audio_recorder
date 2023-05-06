import os, random, time, wave
import threading
import keyboard
import multiprocessing
from audio_recorder import AudioRecorder
import RPi.GPIO as GPIO
import simpleaudio as sa

ar = AudioRecorder()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
answer_directory = "/home/emma/dev/audio_recorder/audio_answers/"
question_directory = "/home/emma/dev/audio_recorder/audio_questions/"


def main_loop():
    global play_obj
    global on_playback
    while True:
        state = GPIO.input(17)
        if on_playback:
            if state == 0:
                on_playback = False;
            elif play_obj == None or not play_obj.is_playing():
                filename = answer_directory+random.choice(os.listdir(answer_directory))
                try:
                    print("About to play " + filename)
                    wav_obj = sa.WaveObject.from_wave_file(filename)
                    play_obj = wav_obj.play()
                except:
                    print("Error playing file")
        else:
            print("Not on playback")
            if play_obj.is_playing():
                play_obj.stop()
            wav_obj = sa.WaveObject.from_wave_file(question_directory+"question.wav")
            play_obj = wav_obj.play()
            play_obj.wait_done()
            ar.record_audio()
            print("audio done recording")
            filename =answer_directory+ ar.get_last_filename()
            wav_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wav_obj.play()
            play_obj.wait_done()
            print("playback also done")
            play_obj = None
            on_playback = True

if __name__ == '__main__':
    global play_obj 
    global on_playback 
    play_obj = None
    on_playback = True
    main_loop()
