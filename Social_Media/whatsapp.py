

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


def whatsapp():

    url = "https://web.whatsapp.com/"
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.click(x=2260, y=226)
    flag = True 
    speak('Search for a person ')
    # while flag:
    # out= listen().lower()
                    
    # if (out != ''):
    #     print(out )
    #     time.sleep(1)
    #     pyautogui.typewrite(out)
    #     flag = False
    #     # pyautogui.typewrite("harshdeep")
    #     pyautogui.press('enter')
    #     time.sleep(2)
    #     pyautogui.click(x=3090, y=1027)  
    #     pyautogui.typewrite("Test")
    #     pyautogui.press('enter')             