import io
import os
import json
import shutil
import aiofiles
from PIL import Image
from fastapi import FastAPI, File, UploadFile
import torch
import whisper
import ffmpeg

app = FastAPI()
model_wis = whisper.load_model("base")
static_dir = os.path.join(os.path.dirname(__file__), "static")

@app.get("/")
async def root():
    return {"this adham alghreeb, i have spoken"}

@app.post("/voicerecog/")
async def voice_recognition(file: UploadFile = File(...)):
    file_path = os.path.join(static_dir, file.filename)
    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    
    result = model_wis.transcribe(file_path)
    return {'results': result}