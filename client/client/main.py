import requests
import pyttsx3

url_home = "http://0.0.0.0:8000/"
url_transcribe = url_home + "transcribe/"
url_transcribe_gr = url_transcribe + "greek"
#url_speak = url_home + "speak/"

if __name__ == "__main__":
    audio_file = "jfk.flac"
    with open(audio_file, 'rb') as audio:
        responce_transcribe = requests.post(url_transcribe_gr, files={"audio_file" : audio})
        print(responce_transcribe.json())
        text = responce_transcribe.json()["text"]
        print(text)
        engine = pyttsx3.init()
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()