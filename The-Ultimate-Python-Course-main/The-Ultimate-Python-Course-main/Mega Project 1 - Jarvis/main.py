import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import sounddevice as sd

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "<Your Key Here>"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def listen_microphone(duration=5):
    sample_rate = 16000

    print("Listening...")

    audio = sd.rec(
        int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16"
    )

    sd.wait()

    audio_bytes = audio.tobytes()

    return sr.AudioData(audio_bytes, sample_rate, 2)


def aiProcess(command):
    client = OpenAI(
        api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a virtual assistant named Jarvis "
                    "skilled in general tasks like Alexa and Google Cloud. "
                    "Give short responses please."
                ),
            },
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message.content


def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):

        song = c.lower().split(" ")[1]

        link = musicLibrary.music[song]

        webbrowser.open(link)

    elif "news" in c.lower():

        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )

        if r.status_code == 200:

            data = r.json()

            articles = data.get("articles", [])

            for article in articles:
                speak(article["title"])

    else:

        output = aiProcess(c)

        speak(output)


if __name__ == "__main__":

    speak("Initializing Jarvis....")

    while True:

        print("recognizing...")

        try:

            audio = listen_microphone(duration=2)

            word = recognizer.recognize_google(audio)

            print("You said:", word)

            if word.lower() == "jarvis":

                speak("Ya")

                audio = listen_microphone(duration=5)

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except sr.UnknownValueError:

            print("Could not understand audio")

        except sr.RequestError as e:

            print("Google Speech Recognition error:", e)

        except Exception as e:

            print("Error:", e)
