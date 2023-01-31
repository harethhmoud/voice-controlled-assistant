import speech_recognition as sr
import subprocess
from datetime import datetime


def recognize():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            transcript = r.recognize_google(audio)
            print("Hmm")
            if 'exit' in transcript or 'stop' in transcript:
                hour = datetime.now().hour
                if (hour >= 21) and (hour < 3):
                    say("Goodnight Hareth")
                else:
                    say("Have a good day!")
                exit()
            else:
                say("Working on it.")
        except sr.UnknownValueError:
            say("Sorry mate didn't get that, can you repeat?")
            transcript = "None"

    return transcript


def say(text):
    subprocess.call(['say', text])


def greet_user():
    hour = datetime.now().hour  # Find the hour to determine the greeting to the user.
    if (hour >= 5) and (hour < 12):
        say("Good morning Hareth")
    elif (hour >= 12) and (hour < 17):
        say("Good afternoon Hareth")
    elif (hour >= 17) and (hour < 19):
        say("Good evening Hareth")
    else:
        "Hello Hareth"
