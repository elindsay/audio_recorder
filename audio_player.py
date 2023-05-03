import os, random, time, wave
import simpleaudio as sa
from playsound import playsound

def play_loop():
    while True:
        print("in play loop")
        files = os.listdir("audio_answers/")
        file = random.choice(files)
        print(file)
        print(files)
        playsound("audio_answers/"+file)


def play_loop():
    file = random.choice(files)
    wave_obj = sa.WaveObject.from_wave_file(file)
    play_obj = wave_obj.play()

def read_gpio():
    last_state = GPIO.input(18)
    #global p
    #p.start()
    while True:
        state = GPIO.input(18)
        if(last_state != state):
            last_state = state
            print("Button pushed") 
            p.terminate()
            playsound("audio_questions/question.wav")
            #p = multiprocessing.Process(target=playsound, args=("audio_questions/question.wav",))
            #p.start()
            #time.sleep(8)
            #p.terminate()
            ar.record_audio()
            filename ="audio_answers/"+ ar.get_last_filename()
            print(filename)
            #p = multiprocessing.Process(target=playsound, args=(filename,))
            #p.start()
            playsound(filename)
            p.terminate()
            p = multiprocessing.Process(target=play_loop)
            p.start()
#threading.Thread(target = play_loop).start()
#threading.Thread(target = read_keystrokes).start()
#threading.Thread(target = read_gpio).start()
#if __name__ == '__main__':
#    #time.sleep(1)
#    read_gpio()
