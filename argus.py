#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This code is based off the original project by Flyingrub : https://github.com/flyingrub/iswod

TODO:

* List a phrase of groupe of words that execute an action
    * "Open door"
    * "Close door"
    * "Turn on the lights"
    * "Turn off the lights"
    * "Play music"
    * "Stop the music"
    * "Next song"
    * "Pause the music"
    
* For each action, define a function to do that

"""
import speech_recognition as sr
import pyaudio
import wave
import sys

fail_counter = 1
open_door = "open the door"
close_door = "close the door"
turn_on_lights = "turn on the lights"
turn_off_lights = "turn the lights off"
play_music = "play music"

def door(state):
    # Import GPIO to open the door.
    if state == "close":
        print("I am now closing the door.")
    elif state == "open":
        print("I am now opening the door.")
    else:
        print("I can't do shit.")

def main():
    global fail_counter
    # Set the language of the recognition
    r = sr.Recognizer(language = "fr-FR")
    m = sr.Microphone()

    while True:
        with m as source:
            print("Listing..")
            audio = r.listen(source)
            try:
                recognised=r.recognize(audio)
                print("You said : %s" % (recognised))
            except LookupError:
                print("I did not understand, could you say that again ?")

        if open_door in recognised.lower():
            print('I got that ! You asked for : %s' % recognised)
            door("open")
        elif close_door in recognised.lower():
            print('I got that ! You asked for : %s' % recognised)
            door("close")
        else:
            pass

if __name__ == "__main__":
    main()