from fastapi import APIRouter, UploadFile, File
from services.ocr_service import extract_text

router = APIRouter()

@router.post("/extract")
async def extract_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    text = extract_text(image_bytes)
    return {"text": text}