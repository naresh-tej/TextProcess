from fastapi import APIRouter, HTTPException
from app.models import TextInput, ProcessedResult
from app.utils import process_text
from typing import List

router = APIRouter()
history = {}

@router.post("/process", response_model=ProcessedResult)
def process(input: TextInput):
    try:
        result = process_text(input.text)
        # Store result in history (optional)
        history[input.text] = result
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[ProcessedResult])
def get_history():
    return list(history.values())
