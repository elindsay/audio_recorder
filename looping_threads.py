#pip install keyboard
import keyboard
import threading, time
import datetime

def read_keystrokes():
    while True:
        key = keyboard.read_event()
        print(key)
        print("yay")
        #key_queue.put(key)O


keystroke_thread = threading.Thread(target=read_keystrokes)
keystroke_thread.start()
def thread1():
    while True:
        print("thread 1")
        time.sleep(1)

def thread2():
    while True:
        print("thread 2")
        time.sleep(2)

threading.Thread(target = thread1).start()
threading.Thread(target = thread2).start()
