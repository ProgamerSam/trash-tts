import os
import time
from datetime import datetime
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import pyautogui
import pyttsx3
from PIL import Image
import torch
import torch as nn



lang = 'en'
now = datetime.now()
guy = ""
engine = pyttsx3.init()

microphone = sr.Microphone(device_index=1)

def get_audio():
    r = sr.Recognizer()
    with microphone as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said
            
            #ask for time function
            if "current time" in guy:
                engine = pyttsx3.init()
                engine.runAndWait()
                
        
        except Exception as Error:
            return None
        return guy

while True:
    if "stop" in guy:
        break
    get_audio()