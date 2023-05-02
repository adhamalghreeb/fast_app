import io
import json
import whisper
import shutil
from PIL import Image
from fastapi import File,FastAPI, UploadFile
import torch
import aiofiles
import pyrebase

model_yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model_wis = whisper.load_model("base")


app = FastAPI()
# just a try and error code ... 
# @app.post("/upload-files")
# async def create_upload_file(file: UploadFile = File(...)):
#     print("filename = ", file.filename) # getting filename
#     destination_file_path = "C:/Users/PC/Desktop/vs_project_1/static/"+file.filename # location to store file
#     async with aiofiles.open(destination_file_path, 'wb') as out_file:
#         while content := await file.read(1024):  # async read file chunk
#             await out_file.write(content)  # async write file chunk

#     return {"Result": "OK"}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# @app.post("/objectdetection/")
# async def root(file: bytes = File(...)):
#   input_image =Image.open(io.BytesIO(file)).convert("RGB") # uploaded to the buffer only
#   results = model_yolo(input_image)
#   results_json =   json.loads(results.pandas().xyxy[0].to_json(orient="records"))
#   return {"result": results_json}

# @app.post("/voicerecog/")
# async def create_upload_file(file: UploadFile = File(...)):
#     destination_file_path = "C:/Users/PC/Desktop/vs_project_1/static/"+file.filename # location to store file
#     async with aiofiles.open(destination_file_path, 'wb') as out_file:
#         while content := await file.read(1024):  # async read file chunk
#             await out_file.write(content)  # async write file chunk
#     var_name = "C:/Users/PC/Desktop/vs_project_1/static/"+file.filename # path to the uploaded file
#     result = model_wis.transcribe(var_name)
#     return {'results': result}