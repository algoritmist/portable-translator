import requests

url="http://0.0.0.0:8000/transcribe"

if __name__ == "__main__":
    audio_file = "jfk.flac"
    with open(audio_file, 'rb') as audio:
        responce = requests.post(url, files={"audio_file" : audio})
        print(responce.json())