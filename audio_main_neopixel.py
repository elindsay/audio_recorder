import os, random, time, wave
import threading
import keyboard
import multiprocessing
from audio_recorder import AudioRecorder
import RPi.GPIO as GPIO
import simpleaudio as sa
import board
import neopixel

ar = AudioRecorder()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

ar = AudioRecorder()

files = os.listdir("audio_answers/")

def main_loop():
    global play_obj
    global on_playback
    global last_input
    while True:
        state = GPIO.input(17)
        if on_playback:
            pixels.fill((255, 255, 0))
            if last_input != state:
                on_playback = False;
                last_input = state
            elif play_obj == None or not play_obj.is_playing():
                filename = "audio_answers/"+random.choice(os.listdir("audio_answers"))
                print("About to play " + filename)
                wav_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wav_obj.play()
        else:
            print("Not on playback")
            pixels.fill((0, 255, 0))
            if play_obj.is_playing():
                play_obj.stop()
            wav_obj = sa.WaveObject.from_wave_file("audio_questions/question.wav")
            play_obj = wav_obj.play()
            play_obj.wait_done()
            ar.record_audio()
            pixels.fill((255, 0, 0))
            print("audio done recording")
            pixels.fill((255, 255, 255))
            filename ="audio_answers/"+ ar.get_last_filename()
            wav_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wav_obj.play()
            play_obj.wait_done()
            print("playback also done")
            play_obj = None
            on_playback = True
            last_input = GPIO.input(17)

if __name__ == '__main__':
    global play_obj 
    global on_playback 
    global last_input
    global pixels
    play_obj = None
    on_playback = True
    last_input = GPIO.input(17)
    pixels = neopixel.NeoPixel(board.D19, 1)
    main_loop()
