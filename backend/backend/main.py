import whisper
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
app_host = "0.0.0.0"
app_port = 8000

tiny_model = whisper.load_model("tiny")


@app.get("/")
async def index():
    """
    Text-to-speech server
    """
    return {"message" : "Speech-to-text server"}

@app.post("/transcribe")
async def trascribe(audio_file: UploadFile = File()):
    contents = await audio_file.read()
    temp_filename = "temp_file.flac.temp"
    with open(temp_filename, "wb") as f:
        f.write(contents)
        f.close()
    result = tiny_model.transcribe(temp_filename)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host=app_host, port=app_port, reload=True)