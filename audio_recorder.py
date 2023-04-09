import os, pyaudio, wave

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 15 # seconds to record
dev_index = 1 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


# create pyaudio stream
class AudioRecorder:
    def __init__(self):
        self.recording = False

    def get_last_filename(self):
        files = os.listdir("audio_answers/")
        files.sort()
        filename = files[-1]
        return filename

    def get_filename(self):
        filename = self.get_last_filename()
        print(filename)
        print(str(int(filename.split("_")[-1].split(".")[0])+1))
        return "audio_answers/audio_"+str(int(filename.split("_")[-1].split(".")[0])+1).zfill(3)+".wav"

    def record_audio(self):
        audio = pyaudio.PyAudio() # create pyaudio instantiation
        if not self.recording:
            self.recording = True
            filename = self.get_filename()
            print(filename)
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


            # save the audio frames as .wav file
            wavefile = wave.open(filename,'wb')
            wavefile.setnchannels(chans)
            wavefile.setsampwidth(audio.get_sample_size(form_1))
            wavefile.setframerate(samp_rate)
            wavefile.writeframes(b''.join(frames))
            wavefile.close()
            self.recording = False

