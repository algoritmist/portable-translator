import requests
from TTS.api import TTS
from TTS.utils.synthesizer import Synthesizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

url_home = "http://0.0.0.0:8000/"
url_transcribe = url_home + "transcribe/"
url_transcribe_en = url_transcribe + "english"
url_transcribe_gr = url_transcribe + "greek"
#url_speak = url_home + "speak/"

synthesizer = Synthesizer()

tts_model = "tts_models/multilingual/multi-dataset/your_tts"
vocoder_model = "vocoder_models/universal/libri-tts/wavegrad"

tts = TTS(model_name=tts_model)

if __name__ == "__main__":
    audio_file = "jfk.flac"
    with open(audio_file, 'rb') as audio:
        responce_transcribe = requests.post(url_transcribe_gr, files={"audio_file" : audio})
        audio.close()
        print(responce_transcribe.json())
        text = responce_transcribe.json()["text"]
        tts.tts_to_file(text=text, file_path="tts_out_file.wav")