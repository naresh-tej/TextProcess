from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="t5-small")

def process_text(text: str) -> dict:
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return {
        "original_text": text,
        "processed_text": summary[0]['summary_text']
    }
