# from Body.listen import listen
# from Body.speak import speak
from Features.clap import Tester

import pygame

 
# def mainx():    

#     Tester()
#     speak("Welcome Sir")

 
# mainx() 


# def wakeUp():
#     queery = listen().lower()
    
#     if "wake up" in queery:
#         pass
    
#     else:
#         pass
    
    

    
pygame.init()

# Initialize pygame mixer with desired parameters
pygame.mixer.init()

import speech_recognition as sr
import os
from jarvis import mainExe
from Body.speak import speak

def listen():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source,0,8)
        
        
    try:
        print("Recognition...")
        query = r.recognize_google(audio,language="en")
        
    except:
        return "" 
    
    query = str(query).lower()
    
    print(query)
    return query


# def wakeUp():

waked = False

while not waked:
    query = listen().lower()
    
    if "wake up" in query:
        pygame.mixer.music.load('computer-processing-sound-effect-01-122131.mp3')  
        pygame.mixer.music.play()
        pygame.time.wait(2000)  # 4000 milliseconds = 4 seconds

        # Stop the sound
        pygame.mixer.music.stop()
        speak("hello sir")
        waked = True
        mainExe()
    
    else:
        print("")
        print("AI : Not started")
        print("")
        pass
    
    
print("Breaked")