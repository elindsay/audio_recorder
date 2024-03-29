import pyaudio

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk


from playsound import playsound
import wave
import sys
#from pynput import keyboard
import keyboard
import threading, time
import datetime



form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 1 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
def record():
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()


class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# https://stackoverflow.com/questions/66196634/loop-until-key-is-pressed-and-repeat
#def loading():
#    while running:
#        print("loading", datetime.datetime.now())

#def on_press(key):
#    global running

#    if key == keyboard.Key.a:
        # stop listener
#        return False

#def on_release(key):
#    global running  # inform function to assign (`=`) to external/global `running` instead of creating local `running`
#    if key == keyboard.Key.b:
#        # to stop loop in thread
#        running = False


#--- main ---

#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join


#while True:
#    # Usage example for pyaudio
#    except KeyboardInterrupt:
#        record()
#    a = AudioFile("test1.wav")
#    a.play()
#    a.close()

def playing_audio():
    while True:
        playsound("//home//emma//dev//audio_recorder//test1.wav")
        time.sleep(3)

def read_keystroke():
    while True:
        key = keyboard.read_event()
        print(key)

threading.Thread(target = playing_audio).start()
keystroke_thread = threading.Thread(target = read_keystroke)
keystroke_thread.start()

while False:
    playsound("//home//emma//dev//audio_recorder//test1.wav")
    key = keyboard.read_event()
    print(key)
