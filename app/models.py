from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
    task: str

class ProcessedResult(BaseModel):
    original_text: str
    processed_text: str
