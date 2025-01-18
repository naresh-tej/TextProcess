# TextProcess

# Text Processing API

## Setup and Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd TextProcess

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    uvicorn app.main:app --reload


The application processes input text using the Hugging Face transformers library's summarization pipeline. Here’s a step-by-step explanation of how it works:

1. Input Submission
The user sends a POST request to the /process endpoint with a JSON payload containing the text to be processed.

Example Input:

json
Copy
Edit
{
  "text": "The quick brown fox jumps over the lazy dog. This is a common English sentence used for testing."
}
2. Input Validation
The TextInput model validates that the input JSON contains a text field and that it is a string.

3. Text Processing
The application uses the summarization pipeline from Hugging Face's transformers library. The summarization model is pre-trained (e.g., t5-small) and processes the input text to generate a summarized version.

Processing:

The summarizer pipeline is called with the input text.
Parameters like max_length and min_length control the length of the generated summary.
do_sample=False ensures deterministic output.
Example Call:

python
Copy
Edit
summary = summarizer("The quick brown fox jumps over the lazy dog. This is a common English sentence used for testing.", max_length=50, min_length=25, do_sample=False)
4. Output Generation
The pipeline returns a summarized version of the input text. The application formats the result into a dictionary containing the original and processed text.

Example Output:

json
Copy
Edit
{
  "original_text": "The quick brown fox jumps over the lazy dog. This is a common English sentence used for testing.",
  "processed_text": "The quick brown fox jumps over the lazy dog, a common English sentence used for testing."
}
5. Storing in History
The result is stored in an in-memory list (history) for future retrieval if the /history endpoint is implemented and used.

Summary
Input: User provides a text string.
Processing: The text is summarized using a pre-trained language model.
Output: The original text and its summarized version are returned to the user.
This approach allows users to leverage advanced natural language processing capabilities through a simple API.