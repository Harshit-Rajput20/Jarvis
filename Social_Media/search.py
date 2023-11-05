


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




def search(query):

    content = query.replace('search','')
    speak('searching' + content)
    pywhatkit.search(content)
    time.sleep(5)
    button_x = 2271
    button_y = 344
    pyautogui.click(button_x, button_y)
    time.sleep(1)
                
    if "stop" in query:
        speak("Stopping automation")
        time.sleep(5)
        button_x = 2271
        button_y = 344
        pyautogui.click(button_x, button_y)
        time.sleep(1)