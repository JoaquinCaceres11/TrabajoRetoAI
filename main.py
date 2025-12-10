from fastapi import FastAPI
from routers.extract import router as extract_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}

app.include_router(extract_router, prefix="/ocr")