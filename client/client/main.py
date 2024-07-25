import requests
from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

url_home = "http://0.0.0.0:8000/"
url_transcribe = url_home + "transcribe/"
url_transcribe_en = url_transcribe + "english"
url_transcribe_fr = url_transcribe + "french"
#url_speak = url_home + "speak/"

tts_model = "tts_models/multilingual/multi-dataset/your_tts"

""" Working tts model paths if you want to add them manualy. Be sure to plase them in ~/.local/share/tts, otherwise you can encounter bugs in api path resolving
tts_path = "~/.local/share/tts/tts_models--multilingual--multi-dataset--your_tts/tts_models/model_file.pth"
config_path = "~/.local/share/tts/tts_models/tts_models--multilingual--multi-dataset--your_tts/config.json"
"""

#tts = TTS(model_path=tts_path, config_path=config_path).to("cpu")
tts = TTS(model_name=tts_model)

if __name__ == "__main__":
    audio_file = "jfk.flac"
    with open(audio_file, 'rb') as audio:
        responce_transcribe = requests.post(url_transcribe_fr, files={"audio_file" : audio})
        audio.close()
        print(responce_transcribe.json())
        text = responce_transcribe.json()["text"]
        tts.tts_to_file(text=text, language="fr-fr", speaker=tts.speakers[0], file_path="tts_out_file.wav")
        #wav = tts.tts(text=text, file_path="tts_out_file.wav")