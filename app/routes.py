from fastapi import APIRouter, HTTPException
from app.models import TextRequest, ProcessedResult
from app.utils import process_text
from typing import List

router = APIRouter()
history = {}

# Initialize LLM pipelines for different tasks
summarization_pipeline = pipeline("summarization")
keyword_extraction_pipeline = pipeline("ner")  # Named Entity Recognition for keyword extraction
sentiment_analysis_pipeline = pipeline("sentiment-analysis")

@router.post("/process", response_model=ProcessedResult)
def process(request: TextRequest):
    try:
        processed_text = ""
        
        if request.task == "summarize":
            result = summarization_pipeline(request.text, max_length=50, min_length=25, do_sample=False)
            processed_text = result[0]['summary_text']
        elif request.task == "keywords":
            result = keyword_extraction_pipeline(request.text)
            processed_text = ", ".join([entity['word'] for entity in result])
        elif request.task == "sentiment":
            result = sentiment_analysis_pipeline(request.text)
            processed_text = result[0]['label']
        else:
            raise HTTPException(status_code=400, detail="Invalid task specified.")
        
        # Store in history
        history.append({"original_text": request.text, "processed_text": processed_text})
        
        return {"original_text": request.text, "processed_text": processed_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[ProcessedResult])
def get_history():
    return list(history.values())
