from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    task: str

class ProcessedResult(BaseModel):
    original_text: str
    processed_text: str
