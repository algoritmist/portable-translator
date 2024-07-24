import whisper
import uvicorn
from fastapi import FastAPI, File, UploadFile


app = FastAPI()
app_host = "0.0.0.0"
app_port = 8000

tiny_model = whisper.load_model("medium")


@app.get("/")
async def index():
    """
    Text-to-speech server
    """
    return {"message" : "Speech-to-text server"}

@app.post("/transcribe/{language_to}")
async def trascribe(language_to: str, audio_file: UploadFile = File()):
    contents = await audio_file.read()
    # TODO: should use other approach for multi-user support
    temp_filename = "temp_file.flac.temp"
    with open(temp_filename, "wb") as f:
        f.write(contents)
        f.close()
    options = dict(language=language_to)
    result = tiny_model.transcribe(temp_filename, **options)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host=app_host, port=app_port, reload=True)