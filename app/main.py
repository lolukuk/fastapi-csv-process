from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from celery import Celery
import pandas as pd
import time

app = FastAPI()

# Настройка Celery
celery_app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
celery_app.config_from_object('app.celeryconfig')

@celery_app.task
def process_file(file_path: str):
    time.sleep(10)  # Имитируем задержку обработки
    df = pd.read_csv(file_path)
    # Выполнение обработки данных
    processed_file_path = file_path.replace('.csv', '_processed.csv')
    df.to_csv(processed_file_path, index=False)
    return processed_file_path

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV files are accepted.")
    file_location = f"app/temp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    process_file.delay(file_location)
    return JSONResponse(content={"message": "File received. Processing started."})

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI file processing service."}
