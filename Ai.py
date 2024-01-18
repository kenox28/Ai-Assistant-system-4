from nltk.chat.util import Chat
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
from patterns import patterns
from reflections import reflections
# from tkinter import *
# from PIL import Image
import sys

class Ai:
    def __init__(self):
        self.name = "Ai Rich"
        self.recognition = sr.Recognizer()
        self.speak = pyttsx3.init()
        self.speak.setProperty('voice', 140)
        self.pat = patterns
        self.ref = reflections
        self.chatbot = Chat(self.pat, reflections)
        self.userneeds = " "
        self.web = " "


    def ONai(self):
        while True:
            with sr.Microphone() as mic:
                print("access ai...")
                self.recognition.pause_threshold = 1
                self.recognition.adjust_for_ambient_noise(mic, duration=0.2)
                recorded = self.recognition.listen(mic)


                self.On = self.recognition.recognize_google(recorded)
                self.On = self.On.lower()
            try:
                if 'hey' in self.On:
                    print('ai is on')
                    self.speak.say(f'activation of {self.name} is on')
                    self.speak.runAndWait()
                    self.identifycommand()
            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
                self.speak.say("Could not understand audio. Please try again.")
                self.speak.runAndWait()
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                self.speak.say("Could not connect to the internet. Please check your connection.")
                self.speak.runAndWait()





    def intro(self):

        # self.aiface()
        self.speak.say(f"hi Im {self.name} what can i do for you")
        self.speak.runAndWait()
    def uservoice(self):
        while True:
            with sr.Microphone() as mic:
                print("Listening...")
                self.recognition.pause_threshold = 1
                self.recognition.adjust_for_ambient_noise(mic, duration=0.1)
                recorded = self.recognition.listen(mic)

            try:
                self.userneeds = self.recognition.recognize_google(recorded)
                self.userneeds = self.userneeds.lower()
                print('loading...')
                return self.userneeds
            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
                self.speak.say("Could not understand audio. Please try again.")
                self.speak.runAndWait()
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                self.speak.say("Could not connect to the internet. Please check your connection.")
                self.speak.runAndWait()

    def identifycommand(self):
        self.intro()
        while True:
            self.userneeds = self.uservoice().lower()
            self.reply = self.chatbot.respond(self.userneeds)
            if 'facebook' in self.userneeds:
                webbrowser.open('https://www.facebook.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()
            elif 'youtube' in self.userneeds:
                webbrowser.open('https://www.youtube.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'instagram' in self.userneeds:
                webbrowser.open('https://www.instagram.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()
            elif 'chat gpt' in self.userneeds:
                webbrowser.open('https://chat.openai.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'twitter' in self.userneeds:
                webbrowser.open('https://twitter.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'linkedin' in self.userneeds:
                webbrowser.open('https://www.linkedin.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'snapchat' in self.userneeds:
                webbrowser.open('https://www.snapchat.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'reddit' in self.userneeds:
                webbrowser.open('https://www.reddit.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'pinterest' in self.userneeds:
                webbrowser.open('https://www.pinterest.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'tiktok' in self.userneeds:
                webbrowser.open('https://www.tiktok.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'github' in self.userneeds:
                webbrowser.open('https://github.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'stackoverflow' in self.userneeds:
                webbrowser.open('https://stackoverflow.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'amazon' in self.userneeds:
                webbrowser.open('https://www.amazon.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'ebay' in self.userneeds:
                webbrowser.open('https://www.ebay.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'netflix' in self.userneeds:
                webbrowser.open('https://www.netflix.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'spotify' in self.userneeds:
                webbrowser.open('https://www.spotify.com')
                self.speak.say(self.reply)
                self.speak.runAndWait()
            elif 'Song' in self.userneeds:
                webbrowser.open('https://www.youtube.com/watch?v=Vvfl0lY4lLQ&list=RDVvfl0lY4lLQ&start_radio=1')
                self.speak.say(self.reply)
                self.speak.runAndWait()


            elif 'close' in self.userneeds:
                pyautogui.hotkey('ctrl', 'w')
                self.speak.say(self.reply)
                self.speak.runAndWait()

            elif 'good bye' in self.userneeds:
                self.speak.say(self.reply)
                self.speak.runAndWait()
                break
            else:
                self.speak.say(self.reply)
                self.speak.runAndWait()

if __name__ == "__main__":
    p = Ai()
    p.ONai()
