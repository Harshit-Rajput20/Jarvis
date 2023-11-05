from Body.speak import speak
from Brains.AI_brain import answers
import speech_recognition as sr
import os
import pywhatkit
import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from bardapi import BardCookies
import datetime
import cv2

from Social_Media.youtube import youtube
from Social_Media.search import search
from Social_Media.whatsapp import whatsapp

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







 
cookie_dict = { 
               "__Secure-1PSID": "cgheJnCZlQGKxf7cRgHWsMKS1H2ot6jzkc4SmkbdTzGz6ByloUDHvP3BhJ39joUhSx43QQ.",
               "__Secure-1PSIDTS": "",
               "__Secure-1PSIDCC": "ACA-OxMIMUwZ4TEBJDx6xkHryIti_Y-SteeGwYCik0MtS50mmBS6swjdPMfyowLKQElCUzqcAV4"
               }
bard = BardCookies(cookie_dict=cookie_dict)


def ReplyBrain(question , chat_log = None):
    Reply = bard.get_answer(question)['content']
    return Reply
            
 
        
            




def mainExe():
    
    speak("I am Friday")
    
    while True:
        query = listen().lower()
        
        if "hello" in query:
            speak("Hi! I am Friday")
        
        elif "friday" in query:
            # print("AI:-" ,query )
            speak("recognizing")        
            question = query.replace('friday','')
            if(len(question)<5):
                speak("invalid question") 
            else:  
                reply = bard.get_answer(question)['content']
                print("Orognal reply :"+reply)
                speak(reply.split(".")[0])          
            
             
            
        elif "youtube" in query:
             
            youtube()    
            
            
            
        elif "search" in query:
            search(query)
             
                 
            
        elif "whatsapp" in query:
            whatsapp()
             
         
        elif "terminal" in query:
            speak("opening terminal")
            os.system('gnome-terminal')
            continue
        elif "libra office" in query:
            speak("opening libra office")
            os.system('libreoffice --writer')  
            
            continue
        elif "firefox" in query:
            speak("opening firefox")
            os.system('firefox')
            continue
        
        elif "camera" in query:
            speak("opening the camera")
            speak("press q for exiting the camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Webcam', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "are you here" in query:
            speak("yes sir")
            
        elif "chat gpt" in query:
            webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")
            
            
        elif  "shutdown" in query or "shut down" in query:
            speak("shutting down the system ,Good by sir")
            os.system("sudo poweroff")
        elif "bye" in query:
            speak("Bye sir have a nice day")
            exit
            

 
            
                    
 

 
            
            
            
            
            
                
            
   
        
        
        
  